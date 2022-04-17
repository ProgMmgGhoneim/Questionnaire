from rest_framework import routers
from django.urls import path

from questionnaire.views.question_view import QuestionViewSet
from questionnaire.views.bussiness_plan_view import BussinessPlanViewSet
from questionnaire.views.answer_view import AnswerViewSet
from questionnaire.views.save_view import save

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'question/', QuestionViewSet, basename='question')
router.register(r'plan', BussinessPlanViewSet, basename='plan')
router.register(r'answer', AnswerViewSet, basename='answer')

urlpatterns = [
    path('save/', save),
]

urlpatterns += router.urls