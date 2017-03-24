from rest_framework import viewsets

from .serializers import *


class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exam.objects.all()

    serializer_class = ExamSerializer


class AssistantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assistant.objects.all()

    serializer_class = AssistantSerializer
