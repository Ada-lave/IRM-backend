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

    class Meta:
        verbose_name = "Тип файла"
        verbose_name_plural = "Тип файлов"
        
    def __str__(self):
        return self.title


class Attachment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя файла")
    path = models.FileField(upload_to="uploads/", verbose_name="Файл")
    material = models.ForeignKey(
        Material,
        related_name="atachments",
        verbose_name="К какому материалу",
        on_delete=models.CASCADE,
    )
    file_type = models.ForeignKey(
        FileType,
        related_name="file_type",
        verbose_name="Тип файла",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        
    def __str__(self):
        return self.name
