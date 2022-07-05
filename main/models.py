from django.db import models


class Film(models.Model):
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    name = models.CharField(max_length=200)
    text = models.TextField()
    screensaver_reference = models.URLField()
    magnet_reference = models.URLField()
