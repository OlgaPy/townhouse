from datetime import datetime

from django.apps import apps
from django.db import connections
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class CardSerializer(ModelSerializer):
    username = serializers.DateField(required=True)

    class Meta:
        model = Card
        # fields = '__all__'
        fields = ('name', 'phone', 'email', 'username')




class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class TownHouseSerializer(ModelSerializer):
    class Meta:
        model = TownHouse
        fields = '__all__'


class ConstructionSerializer(ModelSerializer):
    class Meta:
        model = Construction
        fields = '__all__'


class LocalitySerializer(ModelSerializer):
    class Meta:
        model = Locality
        fields = '__all__'




class MonitorForDateSerializer(serializers.Serializer):
    mode_name = serializers.ChoiceField(choices=('Client-CP', 'Nostro-CP'),
                                        required=True)
    report_date = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    @staticmethod
    def validate_report_date(date) -> str:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except Exception as e:
            raise serializers.ValidationError(
                "Date has wrong format. Use format YYYY-MM-DD")
        return date

class ConstructionStageSerializer(ModelSerializer):
    class Meta:
        model = ConstructionStage
        fields = '__all__'
