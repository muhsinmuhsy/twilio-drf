from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)