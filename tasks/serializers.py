from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Task
        fields = ['id','title','description','completed','created_at','updated_at','owner']
        read_only_fields = ['id','created_at','updated_at','owner']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','password']
    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
