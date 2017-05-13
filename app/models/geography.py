from django.db import models

from app.utils import distance_in_km


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
    MAX_DISTANCE = 200

    name = models.CharField('название', max_length=255)
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    @property
    def university_count(self):
        return len(self.university_set.all())

    @property
    def nearby_universities(self):
        nearby_universities = []
        all_cities = City.objects.all()

        for city in all_cities:
            if (distance_in_km(self.lat, self.lon, city.lat, city.lon) < self.MAX_DISTANCE) and \
                    (city.university_count > 0) and (city.id != self.id):
                nearby_universities += city.university_set.all()

        return nearby_universities

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
