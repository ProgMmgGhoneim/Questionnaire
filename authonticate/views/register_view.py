from rest_framework.permissions import AllowAny
from rest_framework import generics

from authonticate.serializers.register_serializer import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    # TODO ADD THROTTLING
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer