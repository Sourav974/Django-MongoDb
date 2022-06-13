from dataclasses import fields
from rest_framework import serializers
# from template.serializers import *
from .models import *


class SuperBackgroundScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperBackgroundScore
        fields = '__all__'


class SuperComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperComponents
        fields = '__all__'


class SuperTextElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperTextElement
        fields = '__all__'


class SuperLogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperLogos
        fields = '__all__'


class SuperOverlaysSerializer(serializers.ModelSerializer):
    text_element = SuperTextElementSerializer(many=True)
    logos = SuperLogosSerializer(many=True)

    class Meta:
        model = SuperOverlays
        fields = ['text_element', 'logos']


class SuperTemplateSerializer(serializers.ModelSerializer):
    background_score = SuperBackgroundScoreSerializer()
    components = SuperComponentsSerializer(many=True)
    overlays = SuperOverlaysSerializer()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = SuperTemplate
        fields = ['business', 'types', 'duration',
                  'template_url', 'background_score', 'components', 'overlays']

    def get_duration(self, obj):
        return obj.duration.total_seconds()


class CreateSuperTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperTemplate
        fields = '__all__'
