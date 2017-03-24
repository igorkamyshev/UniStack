from django.db import models


class Exam(models.Model):
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return self.name
