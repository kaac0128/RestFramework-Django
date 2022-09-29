from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('id', 'username', 'description', 'email', 'created_at')
		read_only_fields = ('created_at', )