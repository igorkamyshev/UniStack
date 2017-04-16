from django.conf.urls import url

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about', views.AboutView.as_view(), name='about'),
    # География
    url(r'^countries', views.CountryList.as_view(), name='country_list'),
    url(r'^country/(?P<pk>[0-9]+)/$', views.CountryDetail.as_view(), name='country_detail'),
    url(r'^region/(?P<pk>[0-9]+)/$', views.RegionDetail.as_view(), name='region_detail'),
    url(r'^city/(?P<pk>[0-9]+)/$', views.CityDetail.as_view(), name='city_detail'),
    # Университеты
    url(r'universities', views.UniversityList.as_view(), name='university_list'),
    url(r'^university/(?P<pk>[0-9]+)/$', views.UniversityDetail.as_view(), name='university_detail'),
]
