from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from questionnaire.models.bussiness_plan import BussinessPlan


class BussinessPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = BussinessPlan
        exclude = ('created_at', 'updated_at')