from django.db import models


class Exam(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'экзамен'
        verbose_name_plural = 'экзамены'


class NamedLink(models.Model):
    name = models.CharField('название', max_length=255)
    url = models.URLField

    def __str__(self):
        return '{name} ({url})'.format(name=self.name, url=self.url)

    class Meta:
        verbose_name = 'именованая ссылка'
        verbose_name_plural = 'именованные ссылки'


class Assistant(models.Model):
    text = models.TextField('текст')
    title = models.CharField('заголовок', max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'благодарность'
        verbose_name_plural = 'благодарности'


class SocialLink(models.Model):
    name = models.CharField('название социальной сети', max_length=255)
    ur = models.URLField

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'сслыка на социальную сеть'
        verbose_name_plural = 'ссылки на социальные сети'


# География
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
    training_directions = models.ManyToManyField(TrainingDirection)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'


# ВУЗы
class University(models.Model):
    name = models.CharField('название', max_length=255)
    abbr = models.CharField('аббревиатура', max_length=127)
    site = models.URLField('сайт')
    address = models.CharField('адрес главного корпуса', max_length=511, null=True, blank=True)

    hide = models.BooleanField('скрыт', default=True)

    city = models.ForeignKey(City, on_delete=models.PROTECT)

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


# Полдготовительные курсы
class Course(models.Model):
    name = models.CharField('название', max_length=255)
    cost = models.IntegerField('стоимость за семестр')
    percent = models.FloatField('комиссия')
    expiration_date = models.DateField('дата окончания обновления')

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'подготовительные курсы'
        verbose_name_plural = 'подготовительные курсы'
