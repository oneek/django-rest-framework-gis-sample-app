from django.forms import TextInput
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.filters import GeoFilterSet, GeometryFilter

import service_api.models
from service_api.serializers import (CompanySerializer, ServiceAreaSerializer,
                                     ServiceTypeAreaPriceSerializer,
                                     ServiceTypeSerializer)


class CompanyViewSet(ModelViewSet):
    queryset = service_api.models.Company.objects.all()
    serializer_class = CompanySerializer


class ServiceAreaViewSet(ModelViewSet):
    queryset = service_api.models.ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceTypeViewSet(ModelViewSet):
    queryset = service_api.models.ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class RegionFilter(GeoFilterSet):
    contains_geom = GeometryFilter(
        name='area__poly', lookup_expr='contains', widget=TextInput)

    class Meta:
        model = service_api.models.ServiceTypeAreaPrice
        fields = '__all__'


class ServiceTypeAreaPriceViewSet(ModelViewSet):
    queryset = service_api.models.ServiceTypeAreaPrice.objects.all()
    serializer_class = ServiceTypeAreaPriceSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = RegionFilter
    distance_filter_field = 'area'
