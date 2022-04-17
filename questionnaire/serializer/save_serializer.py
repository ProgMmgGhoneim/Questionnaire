from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from questionnaire.models.questionnaire import Questionnaire
from questionnaire.models.question import Question

class QuestionAnswerSerializer(serializers.Serializer):
    question = serializers.CharField(required=True)
    answer = serializers.CharField(required=False,
                                   allow_blank=True)


class SaveSerializer(serializers.Serializer):

    plan_token = serializers.CharField(
        max_length=200,
        required=True)
    questionnaire = serializers.CharField(
        max_length=120,
        required=True)
    question_answer = serializers.ListField(
        child=QuestionAnswerSerializer(many=False),
        required=True)

    def validate(self, data):
        questionnaire = Questionnaire.objects.filter(name=data.get('questionnaire')).last()
        if not questionnaire:
            raise serializers.ValidationError("Questionnaire not Founded")
        
        text = []
        for result in data.get('question_answer'):
            text.append(result.get('question'))
        
        questions = Question.objects.filter(text__in=text, questionnaire=questionnaire)
        if not questions:
            raise serializers.ValidationError("Question not belongs to this Questionnaire ")
        return data
