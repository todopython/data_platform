from django.contrib import admin
from .models import Food  # Food 모델 임포트

admin.site.register(Food)  # Food 모델 등록