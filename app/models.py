from django.db import models


class Exam(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'экзамен'
        verbose_name_plural = 'экзамены'


class Assistant(models.Model):
    text = models.TextField('текст')
    title = models.CharField('заголовок', max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'благодарность'
        verbose_name_plural = 'благодарности'


class Country(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'


class Region(models.Model):
    name = models.CharField('название', max_length=255)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
