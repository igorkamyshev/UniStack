from django.db import models

from . import geography
from . import utils


class Course(models.Model):
    name = models.CharField('название', max_length=255)
    cost = models.IntegerField('стоимость за семестр')
    percent = models.FloatField('комиссия')
    expiration_date = models.DateField('дата окончания обновления')

    city = models.ForeignKey(geography.City, on_delete=models.CASCADE)
    exam = models.ForeignKey(utils.Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'подготовительные курсы'
        verbose_name_plural = 'подготовительные курсы'
