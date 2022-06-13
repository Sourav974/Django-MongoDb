from rest_framework import serializers
from .models import *


class TextBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBox
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoSlot
        fields = '__all__'


class ComponentSerializer2(serializers.ModelSerializer):
    business = serializers.StringRelatedField(many=True)
    # inflection_time = serializers.DecimalField(max_digits=5, decimal_places=2)
    text_box = TextBoxSerializer()
    logo_slot = LogoSerializer()
#

    class Meta:
        model = Component1
        fields = ['id', 'component_url', 'types', 'sub_type', 'length',
                  'business', 'inflection_time', 'text_box', 'logo_slot']


class CreateComponentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Component1
        fields = '__all__'
