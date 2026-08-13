from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    LoginSerializer,
)


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)

            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(
            {'message': 'Logout successful'},
            status=status.HTTP_200_OK
        )