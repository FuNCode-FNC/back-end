from django.db import models
from django.utils import timezone
from django.conf import settings


class Country(models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    name = models.CharField('Страна производства', max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    name = models.CharField('Жанр', max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.name


class Film(models.Model):
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    year_of_release = models.IntegerField()
    date_of_adding = models.DateField(default=timezone.now)
    category = models.ManyToManyField(Category)
    genre = models.ManyToManyField(Genre)
    country = models.ManyToManyField(Country)
    person_who_added = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    screensaver_reference = models.URLField()
    magnet_reference = models.URLField()

    def __str__(self):
        return self.name

