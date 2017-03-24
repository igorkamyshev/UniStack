from rest_framework import serializers

from app.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = [
            'id',
            'name',
        ]
