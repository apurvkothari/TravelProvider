from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, data):
        email = data.get('email','')
        password = data.get('password', '')

        if email and password:
            username=email
            user = authenticate(email=username, password=password)
            print(email)
            print(password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    raise exceptions.ValidationError('user is inactive')
            else:
                raise exceptions.ValidationError('Unable to login with given credentials')

        else:
            raise exceptions.ValidationError('Please insert email and password')