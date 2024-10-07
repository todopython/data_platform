"""
URL configuration for makesomething project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from foodking import views as food_views
from houseking import views as house_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodking/', include('foodking.urls')),  # foodking 앱의 urls.py, 장고는 이렇게 앱별로 따로따로 url을 관리하는게 맞음
    path('houseking/', include('houseking.urls')),  # houseking 앱의 urls.py
]
