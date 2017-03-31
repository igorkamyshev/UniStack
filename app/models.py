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


# Направления подготовки из ФГОС
class TrainingDirectionGroup(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа направлений подготовки ФГОС'
        verbose_name_plural = 'группы направлений подготовки ФГОС'


class TrainingDirection(models.Model):
    name = models.CharField('название', max_length=255)
    url = models.URLField()
    code = models.CharField('код', max_length=255, default='0')
    description = models.TextField('описание', null=True, blank=True)
    intro = models.TextField('интро', null=True, blank=True)

    group = models.ForeignKey(TrainingDirectionGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'направление подготовки ФГОС'
        verbose_name_plural = 'направления подготовки ФГОС'


# Специальности
class SpecialtyGroup(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа специальностей'
        verbose_name_plural = 'группы специальностей'


class Specialty(models.Model):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание', null=True, blank=True)
    intro = models.TextField('интро', null=True, blank=True)
    salary = models.IntegerField('средняя зарплата', default=0)

    group = models.ForeignKey(SpecialtyGroup, on_delete=models.CASCADE)
    training_directions = models.ManyToManyField(TrainingDirection)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'
