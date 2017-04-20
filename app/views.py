from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Country, Region, City, \
    University, \
    TrainingDirectionGroup, TrainingDirection


class IndexView(generic.TemplateView):
    template_name = 'app/index.html'


class AboutView(generic.TemplateView):
    template_name = 'app/index.html'


# География
class CountryList(generic.ListView):
    model = Country
    template_name = 'app/geography/country_list.html'


class CountryDetail(generic.DetailView):
    model = Country
    template_name = 'app/geography/country_detail.html'


class RegionDetail(generic.DetailView):
    model = Region
    template_name = 'app/geography/region_detail.html'


class CityDetail(generic.DetailView):
    model = City
    template_name = 'app/geography/city_detail.html'


# Университеты
class UniversityList(generic.ListView):
    model = University
    template_name = 'app/universities/university_list.html'


class UniversityDetail(generic.DetailView):
    model = University
    template_name = 'app/universities/university_detail.html'


# ФГОС
class TrainingDirectionGroupList(generic.ListView):
    model = TrainingDirectionGroup
    template_name = 'app/fgos/training_direction_group_list.html'


class TrainingDirectionGroupDetail(generic.DetailView):
    model = TrainingDirectionGroup
    template_name = 'app/fgos/training_direction_group_detail.html'


class TrainingDirectionDetail(generic.DetailView):
    model = TrainingDirection
    template_name = 'app/fgos/training_direction_detail.html'
