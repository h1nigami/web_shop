from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Bots
from .serializer import BotsSerializer, UserSerializer
from rest_framework.response import Response


class BotsView(APIView):
    def get(self, request:HttpRequest):
        owner_id = request.GET.get("owner")
        if request.user.is_anonymous:
            return Response(status=401)
        output = [
            {
                "owner": output.owner.username,
                "name": output.name,
                "token": output.token
            } for output in Bots.objects.filter(owner=owner_id)
        ]
        return Response(output)
    
    def post(self, request):
        serializer = BotsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UsersView(APIView):
    def get(self, request:HttpRequest):

        output = [
            {
                "username": output.username,
                "email": output.email
            } for output in User.objects.filter(username=username)
        ]
        return Response(output)
    
    def post(self, request:HttpRequest, username: str):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)