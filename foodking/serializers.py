from rest_framework import serializers
from .models import Food  # Food 모델 import

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food  # 사용할 모델
        fields = '__all__'  # 모든 필드 포함