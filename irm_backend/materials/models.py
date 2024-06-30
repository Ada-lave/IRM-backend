from django.db import models


class Theme(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Темы к тестированию"
        verbose_name_plural = "Темы к тестированию"

    def __str__(self):
        return self.title

class Material(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Материал")

    def __str__(self):
        return self.title[:100]

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"



class FileType(models.Model):
    title = models.CharField(max_length=255)


class Attachment(models.Model):
    path = models.FileField("uploads/")
    material = models.ForeignKey(
        Material,
        related_name="atachments",
        on_delete=models.CASCADE,
    )
    file_type = models.ForeignKey(
        FileType,
        related_name="file_type",
        on_delete=models.CASCADE,
    )


