import logging

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from questionnaire.models.question import Question
from questionnaire.serializer.question_serializer import QuestionSerializer

logger = logging.getLogger(__name__)


class QuestionViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """Get all questions or questions filterd by text, category and questionnaire_name

        Returns:
            obj: Qusetion query set
        """
        query_param = self.request.data
        text = query_param.get('text', None)
        category__name = query_param.get('category_name', None)
        questionnaire__name = query_param.get('questionnaire_name', None)

        logger.debug('[QUESTION][LIST] request data {}'.format(query_param))

        if text or category__name or questionnaire__name:
            return Question.objects.filter(Q(text=text) |
                                           Q(category__name=category__name) |
                                           Q(questionnaire__name=questionnaire__name))
            
        return super(QuestionViewSet, self).get_queryset()

    def create(self, request):
        """
            Create Question basicly with only text
        """
        if not self.request.user.has_perm('question.can_add_question'):
            return Response(data={"message": "Permission Denied"},
                            status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = QuestionSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data={"message": "Question Created Successfully"},
                        status=status.HTTP_201_CREATED)
