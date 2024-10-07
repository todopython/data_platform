from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='houseking'),  # 기본 경로에 대한 뷰
]