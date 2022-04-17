from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from authonticate.serializers.token_serializer import TokenSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer