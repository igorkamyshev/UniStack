from django.db import models

from . import geography


class University(models.Model):
    name = models.CharField('название', max_length=255)
    abbr = models.CharField('аббревиатура', max_length=127)
    logo = models.ImageField(upload_to='university_logo/', default='logo_default.png')

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


class Rating(models.Model):
    name = models.CharField('название', max_length=511)
    source = models.URLField('адрес источника')
    year = models.IntegerField('год сбора информации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'


class RatingPosition(models.Model):
    position = models.IntegerField('позиция в рейтинге')
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return('{rating}, {university}: {position} позиция'.format(
            rating=self.rating.name,
            university=self.university.abbr,
            position=self.position))

    class Meta:
        verbose_name = 'позиция в рейтинге'
        verbose_name_plural = 'позиции в рейтинге'