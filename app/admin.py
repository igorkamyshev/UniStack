from django.contrib import admin

from .models import Exam, Assistant, Country, Region, City, TrainingDirectionGroup, TrainingDirection

admin.site.register(Exam)

admin.site.register(Assistant)

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)

admin.site.register(TrainingDirectionGroup)
admin.site.register(TrainingDirection)

