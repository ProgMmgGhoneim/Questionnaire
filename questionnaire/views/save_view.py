import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from questionnaire.models.questionnaire import Questionnaire
from questionnaire.models.question import Question
from questionnaire.models.response import QResponse
from questionnaire.models.bussiness_plan import BussinessPlan
from questionnaire.models.answer import Answer
from questionnaire.serializer.save_serializer import SaveSerializer

logger = logging.getLogger(__name__)


@api_view(['Post'])
@permission_classes([IsAuthenticated])
def save(request, format=None):
    """
        Validata sent data
        create response to save user and it's questionnaire
        Save merchant question and it's answer
    """
    data = request.data
    logger.debug('[SAVE] request data {}'.format(data))

    # Check sent data
    serializer = SaveSerializer(data=data)
    if not serializer.is_valid():
        return Response(data={"message": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
    # get bussiness plan from plan token
    bussiness_plane = BussinessPlan.from_auth_token(
        token=serializer.validated_data['plan_token'])
    
    logger.debug('[SAVE] plans belongs to token {} is {}'.format(serializer.validated_data['plan_token'],
                                                                 bussiness_plane))
    
    # Create response
    response = QResponse.objects.create(
        questionnaire=Questionnaire.objects.get(
            name=serializer.validated_data['questionnaire']),
        bussiness_plane=bussiness_plane
    )
    logger.debug('[SAVE] response for bussiness plan {} is {} '.format(bussiness_plane.id,
                                                                       response.id))
    
    # Get Question
    answers = []
    for question in serializer.validated_data['question_answer']:
        answers.append(
            Answer(question=Question.objects.get(text=question.get('question')),
                   answer=question.get('answer'),
                   response=response)
        )
    logger.debug('[SAVE] answer for bussiness plan {} is {} '.format(bussiness_plane.id,
                                                                       answers))

    Answer.objects.bulk_create(answers)

    return Response(data={"message": "Saved"},
                    status=status.HTTP_200_OK)
