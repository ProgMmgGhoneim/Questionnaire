import logging

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from questionnaire.models.answer import Answer
from questionnaire.models.response import QResponse
from questionnaire.models.bussiness_plan import BussinessPlan
from questionnaire.serializer.bussiness_plane_serializer import BussinessPlanSerializer
from questionnaire.serializer.answer_serializer import AnswerSerializer

logger = logging.getLogger(__name__)


class BussinessPlanViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = BussinessPlan.objects.all()
    serializer_class = BussinessPlanSerializer

    def create(self, request):
        """
            Create Bussiness Plan basicly with only text
        """
        data = self.request.data
        serializer = BussinessPlanSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        bussiness_plan = serializer.instance
        response = {
            "message": "Bussiness Plan Created Successfully",
            "plan_id": bussiness_plan.id,
            "plan_token": bussiness_plan.generate_auth_token()
        }
        return Response(data=response,
                        status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def questions(self, request):
        """
            Get the question of merchant bussiness plan
            to confirm the selected questionnaire
        """
        data = self.request.data

        logger.debug('[BUSSINESS-PLAN][QUESTION] request data {}'.format(data))
        paln_token = data.get("plan_token")
        if not paln_token:
            return Response(data={"message": "Please Enter the valid data."},
                            status=status.HTTP_400_BAD_REQUEST)
        response = QResponse.objects.filter(
            bussiness_plane=BussinessPlan.from_auth_token(paln_token))

        logger.debug('[BUSSINESS-PLAN][QUESTION] response id {}'.format(response))

        answer = Answer.objects.filter(
            response__in=response
        )
        
        logger.debug('[BUSSINESS-PLAN][QUESTION] answer id {}'.format(answer))
        
        return Response(data=AnswerSerializer(answer, many=True).data,
                        status=status.HTTP_200_OK)
