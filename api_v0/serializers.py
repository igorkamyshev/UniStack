from rest_framework import serializers

from app.models import Exam, Assistant


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
