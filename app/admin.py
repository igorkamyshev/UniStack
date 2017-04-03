from django.contrib import admin

from .models import *


# Экзамены
admin.site.register(Exam)


# Благодарности
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


# Напраления подготовки по ФГОС
class TrainingDirectionInLine(admin.TabularInline):
    model = TrainingDirection


class TrainingDirectionGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                ]
            }
        ),
    ]
    inlines = [TrainingDirectionInLine]

admin.site.register(TrainingDirectionGroup, TrainingDirectionGroupAdmin)


# Полдготовительные курсы
admin.site.register(Course)

