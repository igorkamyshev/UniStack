from django.conf.urls import url

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(), name='index'),
    url(r'^about',
        views.AboutView.as_view(), name='about'),
    # География
    url(r'^countries',
        views.CountryList.as_view(), name='country_list'),
    url(r'^country/(?P<pk>[0-9]+)/$',
        views.CountryDetail.as_view(), name='country_detail'),
    url(r'^region/(?P<pk>[0-9]+)/$',
        views.RegionDetail.as_view(), name='region_detail'),
    url(r'^city/(?P<pk>[0-9]+)/$',
        views.CityDetail.as_view(), name='city_detail'),
    # Университеты
    url(r'universities',
        views.UniversityList.as_view(), name='university_list'),
    url(r'^university/(?P<pk>[0-9]+)/$',
        views.UniversityDetail.as_view(), name='university_detail'),
    url(r'subdivision/(?P<pk>[0-9]+)/$',
        views.SubdivisionDetail.as_view(), name='subdivision_detail'),
    # ФГОС
    url(r'training_direction_groups',
        views.TrainingDirectionGroupList.as_view(), name='training_direction_group_list'),
    url(r'training_direction_group/(?P<pk>[0-9]+)/$',
        views.TrainingDirectionGroupDetail.as_view(), name='training_direction_group_detail'),
    url(r'training_direction/(?P<pk>[0-9]+)/$',
        views.TrainingDirectionDetail.as_view(), name='training_direction_detail'),
]
