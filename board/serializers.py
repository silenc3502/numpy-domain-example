from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField()  # 작성자의 username을 포함합니다.

    class Meta:
        model = Board
        fields = '__all__'
