from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from service_api.models import (Company, ServiceArea, ServiceType,
                                ServiceTypeAreaPrice)


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    company = CompanySerializer()

    def create(self, validated_data):
        company_serializer = CompanySerializer(
            data=validated_data.pop('company'))
        if company_serializer.is_valid():
            company = company_serializer.save()
            validated_data['company'] = company
        res, created = self.Meta.model.objects.get_or_create(**validated_data)
        return res

    class Meta:
        model = ServiceArea
        fields = '__all__'
        geo_field = 'poly'


class ServiceAreaSearchSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'
        geo_field = 'poly'


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class ServiceTypeAreaPriceSerializer(ModelSerializer):
    area = ServiceAreaSerializer()

    def create(self, validated_data):
        st_serializer = ServiceAreaSerializer(
            data=validated_data.get('area', None))
        if st_serializer.is_valid(raise_exception=False):
            area = st_serializer.save()
            validated_data['area'] = area
        res = self.Meta.model.objects.create(**validated_data)
        return res

    class Meta:
        model = ServiceTypeAreaPrice
        fields = '__all__'
