from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import FoodViewSet

router = DefaultRouter()
router.register(r'api/foods', FoodViewSet, basename='food')

urlpatterns = [
    path('', views.index, name='foodking'),  # 기본 경로에 대한 뷰
    path('', include(router.urls)),  # DRF API 뷰 추가
]