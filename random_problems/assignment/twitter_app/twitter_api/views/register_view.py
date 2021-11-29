from logging import raiseExceptions
from django.http import response
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        payload = request.data

        print(payload)

        username = payload['username']
        password = payload['password']

        if password == "":
            return Response(data="Password cannot be blank", status=status.HTTP_400_BAD_REQUEST)

        try:

            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                return Response(data = {'username':user.username,'token':token.key},status=status.HTTP_201_CREATED)
            else:
                return Response(data="User exists already",status=status.HTTP_409_CONFLICT)

        except Exception as e:

            print(e)
            return Response(data = "Something went wrong !",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
