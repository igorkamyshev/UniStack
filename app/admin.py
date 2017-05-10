import nested_admin
from django.contrib import admin

from .models import *

# Экзамены
admin.site.register(Exam)


# Благодарности
admin.site.register(Assistant)


# Полдготовительные курсы
admin.site.register(Course)


# География (города, регионы, страны)
class CityInline(admin.TabularInline):
    model = City


class RegionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'country']}),
    ]
    inlines = [CityInline]

admin.site.register(Country)
admin.site.register(Region, RegionAdmin)


# Напраления подготовки по ФГОС
class TrainingDirectionInline(admin.StackedInline):
    model = TrainingDirection


class TrainingDirectionGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [TrainingDirectionInline]

admin.site.register(TrainingDirectionGroup, TrainingDirectionGroupAdmin)


# Специальности
class SpecialityInline(admin.StackedInline):
    model = Speciality


class SpecialityGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [SpecialityInline]

admin.site.register(SpecialityGroup, SpecialityGroupAdmin)


# ВУЗы
class DepartmentInline(nested_admin.NestedTabularInline):
    model = Department


class SubdivisionInline(nested_admin.NestedStackedInline):
    model = Subdivision
    inlines = [DepartmentInline]


class RatingPositionInline(nested_admin.NestedStackedInline):
    model = RatingPosition
    extra = 1


class UniversityAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'abbr', 'parent', 'logo']}),
        ('Контакты',    {'fields': ['city', 'site', 'address']}),
        ('Отображение', {'fields': ['hide']}),
    ]
    inlines = [SubdivisionInline, RatingPositionInline]

admin.site.register(University, UniversityAdmin)


# Рейтинги
class RatingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'source', 'year']}),
    ]
    inlines = [RatingPositionInline]


admin.site.register(Rating, RatingAdmin)
