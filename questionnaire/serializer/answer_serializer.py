from rest_framework import serializers

from questionnaire.models.answer import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = ('created_at', 'updated_at')

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "answer": instance.answer,
            "question": instance.question.text,
            "can_edit": instance.response.questionnaire.editable_answers,
            "questionnaire": instance.response.questionnaire.name
        }


class AnswerUpdateSerializer(serializers.Serializer):
    answer = serializers.CharField(required=True)
    
    def update(self, answer, validated_data):
        """
        Update the question answer

        Args:
            answer (obj): question and answer objects
            validated_data (dict): {"answer": "....."}

        Returns:
            answer objects
        """
        # check if question cand be edit
        if not answer.response.questionnaire.editable_answers: 
            raise serializers.ValidationError("This question can't be edit")

        answer.answer = validated_data['answer']
        answer.save()
        return answer