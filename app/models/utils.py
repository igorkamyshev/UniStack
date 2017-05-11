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


class NamedLink(models.Model):
    """
    Абстрактный класс для всех именованных ссылок
    """
    name = models.CharField('название', max_length=255)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return '{name} ({url})'.format(name=self.name, url=self.url)

    class Meta:
        verbose_name = 'именованая ссылка'
        verbose_name_plural = 'именованные ссылки'
        abstract = True
