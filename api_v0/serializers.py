from rest_framework import serializers

from app.models import Exam, Assistant, TrainingDirection, TrainingDirectionGroup


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
            'intro'
        ]


class TrainingDirectionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDirectionGroup
        fields = [
            'name'
        ]
