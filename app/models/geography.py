from django.db import models


class Country(models.Model):
    name = models.CharField('название', max_length=255)

    @property
    def university_count(self):
        count = 0
        for region in self.region_set.all():
            count += region.university_count
        return count

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'


class Region(models.Model):
    name = models.CharField('название', max_length=255)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    @property
    def university_count(self):
        count = 0
        for city in self.city_set.all():
            count += city.university_count
        return count

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'


class City(models.Model):
    name = models.CharField('название', max_length=255)
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    @property
    def university_count(self):
        return len(self.university_set.all())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
