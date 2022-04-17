from django.contrib import admin

from questionnaire.models.question import Question
from questionnaire.models.category import Category
from questionnaire.models.answer import Answer
from questionnaire.models.questionnaire import Questionnaire
from questionnaire.models.response import QResponse
from questionnaire.models.bussiness_plan import BussinessPlan

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Questionnaire)
admin.site.register(QResponse)
admin.site.register(BussinessPlan)