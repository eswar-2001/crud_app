from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserCredential
from .serializers import UserCredentialSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/user-list/',
        'Detail View': '/user-detail/<str:pk>/',
        'Create': '/user-create/',
        'Update': '/user-update/<str:pk>',
        'Delete': 'user-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users=UserCredential.objects.all()
    serializer = UserCredentialSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user=UserCredential.objects.get(id=pk)
    serializer = UserCredentialSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
	serializer = UserCredentialSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
    user = UserCredential.objects.get(id=pk)
    serializer = UserCredentialSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def userDelete(request, pk):
    user = UserCredential.objects.get(id=pk)
    user.delete()

    return Response("Item Successfully deleted")