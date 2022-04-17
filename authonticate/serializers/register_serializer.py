from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from authonticate.models.merchant import Merchant


class RegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField(
        max_length=120,
        allow_blank=False,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password])
    password2 = serializers.CharField(
        write_only=True,
        required=True)
    email = serializers.CharField(
        max_length=120,
        required=True)
    is_active = serializers.NullBooleanField(
        required=False,
        default=False)

    def validate(self, attrs):
        """
            Validate if password equla password2
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    @transaction.atomic()
    def create(self, validated_data):
        """
        Used to create user and merchant object

        Args:
            validated_data (dict): data sent 

        Returns:
            obj: user
        """
        user = User(username=validated_data.get('username'), 
                    email=validated_data.get('email')
                    )
        user.set_password(validated_data.get('password'))
        user.save()
        merchant = Merchant(
            user=user,
            active_merchant=validated_data.get('is_active', True),
        )
        merchant.save()
        return user

    @transaction.atomic()
    def update(self, merchnat, validated_data):
        user = merchnat.user
        user.set_password(validated_data.get('username'))
        user.save()
        
        merchnat.active_merchant=validated_data.get('is_active')
        merchnat.save()

        return user