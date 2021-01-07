from abc import ABC

from rest_framework import serializers

from blog.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'full_name', 'is_staff', 'is_active', 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

