from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer, LoginSerializer
from django.contrib.auth import login, logout
from .opt import *


class RegisterView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=UserSerializer(data=data)
            print("before Otp ")
            if serializer.is_valid():
                pass
                #sent_otp_email(serializer.data['email'])
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status':200,
                        'message':'Registration Successfull',
                        'data':data
                    }
                )
            return Response(
                 {
                     'status':400,
                     'message':'Something went wrong',
                     'data':serializer.errors
                 }
             )
        except Exception as e:
            print(e)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        logout(request)
        return Response(status=200)

