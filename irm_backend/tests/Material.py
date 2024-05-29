from django.db import models


class Material(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title[:100]

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
