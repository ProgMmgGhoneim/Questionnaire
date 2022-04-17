from rest_framework import serializers

from questionnaire.models.response import QResponse

class QResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QResponse
        fields = '__all__' 