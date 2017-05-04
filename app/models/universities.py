from django.db import models

from . import geography


class University(models.Model):
    name = models.CharField('название', max_length=255)
    abbr = models.CharField('аббревиатура', max_length=127)
    site = models.URLField('сайт')
    address = models.CharField('адрес главного корпуса', max_length=511, null=True, blank=True)

    hide = models.BooleanField('скрыт', default=True)

    city = models.ForeignKey(geography.City, on_delete=models.PROTECT)

    @property
    def region(self):
        return self.city.region

    @property
    def country(self):
        return self.city.region.country

    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ВУЗ'
        verbose_name_plural = 'ВУЗы'


class Subdivision(models.Model):
    name = models.CharField('название', max_length=255)
    abbr = models.CharField('аббревиатура', max_length=127)
    site = models.URLField('сайт')

    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'институт/факультет'
        verbose_name_plural = 'институты/факультеты'


class Department(models.Model):
    name = models.CharField('название', max_length=255)
    site = models.URLField('сайт')

    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'кафедра'
        verbose_name_plural = 'кафедры'
