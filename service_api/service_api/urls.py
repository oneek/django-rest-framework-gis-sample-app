"""service_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from service_api import views

app = apps.get_app_config('service_api')

for model_name, model in app.models.items():
    admin.site.register(model)

router = DefaultRouter()

router.register(r'company', views.CompanyViewSet)
router.register(r'servicearea', views.ServiceAreaViewSet)
router.register(r'servicetype', views.ServiceTypeViewSet)
router.register(r'servicetypeareaprice', views.ServiceTypeAreaPriceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
