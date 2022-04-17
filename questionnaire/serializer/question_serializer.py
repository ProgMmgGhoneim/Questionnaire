from questionnaire.models.questionnaire import Questionnaire
from rest_framework import serializers

from questionnaire.models.question import Question

class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    questionnaire = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        exclude = ('created_at', 'updated_at')
        
    def get_category(self, obj):
        return obj.category.name if obj.category else None
    
    def get_questionnaire(self, obj):
        return obj.questionnaire.name if obj.questionnaire else None