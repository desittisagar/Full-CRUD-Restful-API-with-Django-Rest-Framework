from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import rest_api_model
from .serializers import TodolistSerializer


# Create your views here.

class TodoListCollection(APIView):

	def get(self, request):
		items = rest_api_model.objects.all()
		serializer = TodolistSerializer(items, many = True)
		return Response(serializer.data)

	def post(self, request):
		serializer = TodolistSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)		


class TodoListDetail(APIView):

	def get(self, request, pk):
		items = rest_api_model.objects.get(id = pk)
		serializer = TodolistSerializer(items)
		return Response(serializer.data)


	def delete(self, request, pk):
		item = rest_api_model.objects.get(id = pk)
		item.delete()
		return Response(status.status.HTTP_204_NO_CONTENT)

	def put(self, request, pk):
		item = rest_api_model.objects.get(id = pk)
		serializer = TodolistSerializer(item, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)	
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
