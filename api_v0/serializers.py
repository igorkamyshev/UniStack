from rest_framework import serializers

from app.models import *


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = [
            'id',
            'name',
        ]


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = [
            'id',
            'text',
            'title',
            'url',
        ]


class TrainingDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDirection
        fields = [
            'name',
            'url',
            'code',
            'description',
            'intro',
            'group',
        ]


class TrainingDirectionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDirectionGroup
        fields = [
            'name',
        ]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'name',
        ]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'name',
            'country',
        ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
            'region',
            'lat',
            'lon',
        ]
