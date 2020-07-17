from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fullthrottle.apps.login.serializers import SignUpSerializer, LoginSerializer


@api_view(['POST'])
@csrf_exempt
def register(request):
    try:
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            if not User.objects.filter(username=serializer.validated_data.get('username')).exists():
                User.objects.create_user(**serializer.validated_data)
                user = authenticate(
                    username=serializer.validated_data.get('username'),
                    password=serializer.validated_data.get('password'))
                if user is not None:
                    token, create_or_fetch = Token.objects.get_or_create(
                        user=user)
            else:
                return Response(
                    {'message': "Username already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as ex:
        return Response(
            {'message': 'Please provide proper input'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@csrf_exempt
@api_view(['POST'])
def login(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data.get('username'),
                password=serializer.validated_data.get('password')
            )
            if user is not None:
                token, create_or_fetch = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'message': "Invalid Credentials"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as ex:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response(
            {'message': 'Logged off successfully'},
            status=status.HTTP_200_OK)
    except Exception as ex:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
