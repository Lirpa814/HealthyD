"""HealthyD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from membership import views

urlpatterns = [
    url('^$', views.login_page),
    path('admin/', admin.site.urls),
    path('app_login/', views.app_login),
    path('app_get_info/', views.app_get_info),
    path('app_post_info/', views.app_post_info),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
