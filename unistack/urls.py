from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('front.urls')),
    url(r'^api/v0/', include('api_v0.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin_tools/', include('admin_tools.urls')),
]
