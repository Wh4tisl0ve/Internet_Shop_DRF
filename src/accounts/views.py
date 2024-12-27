from django.contrib.auth import get_user_model, authenticate, login, logout

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"detail": "Login successful"}, status=200)
        else:
            return Response({"detail": "Invalid credentials"}, status=401)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logout successful"}, status=200)
