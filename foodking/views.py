from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Food
from .serializers import FoodSerializer

# 기존 HTML 뷰
def index(request):
    return render(request, 'foodking/index.html')

# DRF ViewSet
class FoodViewSet(viewsets.ViewSet):
    queryset = Food.objects.all()  # queryset 속성 추가 ViewSet을 사용할 때는 일반적으로 queryset 속성정의
    def list(self, request):
        queryset = Food.objects.all()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)