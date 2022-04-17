import logging

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from questionnaire.models.answer import Answer
from questionnaire.serializer.answer_serializer import AnswerUpdateSerializer

logger = logging.getLogger(__name__)


class AnswerViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerUpdateSerializer

    def update(self, request, pk=None):
        try:
            answer = Answer.objects.get(id=pk)
        except:
            return Response(data={"message": " Answer is not exsits"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        data = self.request.data
        serializer = AnswerUpdateSerializer(answer, data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        logger.debug('[ANSWER][UPDATE] Answer {} Updated Successfully'.format(answer.id))
        serializer.save()
        return Response(data={"message": "Answer Updated Successfully"},
                        status=status.HTTP_200_OK)
