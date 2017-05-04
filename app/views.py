from django.views import generic

from .models import Country, Region, City, \
    University, Subdivision, \
    TrainingDirectionGroup, TrainingDirection
from .utils import distance_in_km


class IndexView(generic.TemplateView):
    template_name = 'app/index.html'


class AboutView(generic.TemplateView):
    template_name = 'app/about.html'


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

    MAX_DISTANCE = 200

    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)

        context['nearby_cities'] = []
        all_cities = City.objects.all()

        lat = context['object'].lat
        lon = context['object'].lon

        for city in all_cities:
            if (distance_in_km(lat, lon, city.lat, city.lon) < self.MAX_DISTANCE) and \
                    (city.university_count > 0) and (city.id != context['object'].id):
                context['nearby_cities'].append(city)

        return context


# Университеты
class UniversityList(generic.ListView):
    model = University
    template_name = 'app/universities/university_list.html'


class UniversityDetail(generic.DetailView):
    model = University
    template_name = 'app/universities/university_detail.html'


class SubdivisionDetail(generic.DetailView):
    model = Subdivision
    template_name = 'app/universities/subdivision_detail.html'


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
