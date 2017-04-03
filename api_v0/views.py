from rest_framework import viewsets

from .serializers import *


class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exam.objects.all()

    serializer_class = ExamSerializer


class AssistantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assistant.objects.all()

    serializer_class = AssistantSerializer


class TrainingDirectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrainingDirection.objects.all()

    serializer_class = TrainingDirectionSerializer


class TrainingDirectionGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrainingDirectionGroup.objects.all()

    serializer_class = TrainingDirectionGroupSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()

    serializer_class = CountrySerializer


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()

    serializer_class = RegionSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()

    serializer_class = CitySerializer
