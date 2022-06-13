from dataclasses import fields
from rest_framework import serializers
from .models import *


class BackgroundScoreSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = BackgroundScore
        fields = ['id', 'score_url', 'start_time', 'end_time']

    def get_start_time(self, obj):
        return obj.start_time.total_seconds()

    def get_end_time(self, obj):
        return obj.start_time.total_seconds()


class TextElementSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = TextElement
        fields = ['text', 'font', 'font_size', 'position_x',
                  'position_y', 'start_time', 'end_time']

    def get_start_time(self, obj):
        return obj.start_time.total_seconds()

    def get_end_time(self, obj):
        return obj.start_time.total_seconds()


class LogosSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = Logos
        fields = ['logo_url', 'start_time', 'end_time',
                  'transition_in', 'transition_out']

    def get_start_time(self, obj):
        return obj.start_time.total_seconds()

    def get_end_time(self, obj):
        return obj.start_time.total_seconds()


class OverlaysSerializer(serializers.ModelSerializer):
    text_element = TextElementSerializer(many=True)
    logos = LogosSerializer(many=True)

    class Meta:
        model = Overlays
        fields = ['logos', 'text_element']


class ComponentsSerializer(serializers.ModelSerializer):
    component_start_time = serializers.SerializerMethodField()

    class Meta:
        model = Components
        fields = ['slot_id', 'component_url', 'component_start_time']

    def get_component_start_time(self, obj):
        return obj.component_start_time.total_seconds()


class TemplateSerializer(serializers.ModelSerializer):

    background_score = BackgroundScoreSerializer()
    overlays = OverlaysSerializer()
    components = ComponentsSerializer()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Template
        fields = ['id', 'business', 'types', 'watermark', 'duration',
                  'template_url', 'background_score', 'components', 'overlays']

    def get_duration(self, obj):
        return obj.duration.total_seconds()


class CreateTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = '__all__'
