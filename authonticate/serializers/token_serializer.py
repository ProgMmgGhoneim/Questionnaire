from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authonticate.models.merchant import Merchant

class TokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        try:
            data['merchant_id'] = Merchant.objects.get(user=self.user).id
        except BaseException:
            raise serializers.ValidationError("User isn't merchant")
        return data
    
    @classmethod
    def get_token(cls, user):
        """
            Get token from super class and append username and email to token
        """
        token = super(TokenSerializer, cls).get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        return token