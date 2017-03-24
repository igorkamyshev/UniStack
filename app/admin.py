from django.contrib import admin

from .models import Exam, Assistant, Country, Region, City, TrainingDirectionGroup, TrainingDirection

admin.site.register(Exam)

admin.site.register(Assistant)


# География (города, регионы, страны)
class CityInLine(admin.TabularInline):
    model = City


class RegionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'country',
                ]
            }
        ),
    ]
    inlines = [CityInLine]

admin.site.register(Country)
admin.site.register(Region, RegionAdmin)

admin.site.register(TrainingDirectionGroup)
admin.site.register(TrainingDirection)

