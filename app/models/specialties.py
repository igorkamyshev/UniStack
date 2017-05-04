from django.db import models

from . import fgos


class SpecialityGroup(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа специальностей'
        verbose_name_plural = 'группы специальностей'


class Speciality(models.Model):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание', null=True, blank=True)
    intro = models.TextField('интро', null=True, blank=True)
    salary = models.IntegerField('средняя зарплата', default=0)

    group = models.ForeignKey(SpecialityGroup, on_delete=models.CASCADE)
    training_directions = models.ManyToManyField(fgos.TrainingDirection)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'
