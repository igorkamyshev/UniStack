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
class CityInLine(admin.TabularInline):
    model = City


class RegionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'country']}),
    ]
    inlines = [CityInLine]

admin.site.register(Country)
admin.site.register(Region, RegionAdmin)


# Напраления подготовки по ФГОС
class TrainingDirectionInLine(admin.StackedInline):
    model = TrainingDirection


class TrainingDirectionGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [TrainingDirectionInLine]

admin.site.register(TrainingDirectionGroup, TrainingDirectionGroupAdmin)


# Специальности
class SpecialityInLine(admin.StackedInline):
    model = Speciality


class SpecialityGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [SpecialityInLine]

admin.site.register(SpecialityGroup, SpecialityGroupAdmin)


# ВУЗы
class DepartmentInLine(nested_admin.NestedTabularInline):
    model = Department


class SubdivisionInLine(nested_admin.NestedStackedInline):
    model = Subdivision
    inlines = [DepartmentInLine]


class RatingPositionInline(nested_admin.NestedStackedInline):
    model = RatingPosition
    extra = 1


class UniversityAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'abbr', 'parent']}),
        ('Контакты',    {'fields': ['city', 'site', 'address']}),
        ('Отображение', {'fields': ['hide']}),
    ]
    inlines = [SubdivisionInLine, RatingPositionInline]

admin.site.register(University, UniversityAdmin)


# Рейтинги
class RatingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'source', 'year']}),
    ]
    inlines = [RatingPositionInline]


admin.site.register(Rating, RatingAdmin)
