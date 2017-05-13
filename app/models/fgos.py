from django.db import models


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
