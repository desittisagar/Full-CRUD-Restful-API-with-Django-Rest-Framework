from rest_framework import serializers
from .models import rest_api_model

class TodolistSerializer(serializers.ModelSerializer):

	class Meta:
		model = rest_api_model
		fields = "__all__"