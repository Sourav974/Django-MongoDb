from rest_framework import serializers
from .models import *


class InflectionTimeSerializer(serializers.ModelSerializer):
    data_field = serializers.SerializerMethodField()

    class Meta:
        model = InflectionTime
        fields = ['data_field']

    def get_data_field(self, obj):
        return obj.data_field.total_seconds()


class ComponentSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField(many=True)
    inflection_time = InflectionTimeSerializer(many=True)
    # length = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ['id', 'component_url', 'types', 'sub_type','business', 'inflection_time']

    # def get_inflection_time(self, obj):
    #     return obj.inflection_time.total_seconds()

    def get_length(self, obj):
        return obj.length.total_seconds()


class ComponentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'
