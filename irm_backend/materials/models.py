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


class AttachmentType(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Тип прикрепления"
        verbose_name_plural = "Тип прикреплений"
        
    def __str__(self):
        return self.title


class Attachment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя файла")
    path = models.FileField(upload_to="static/uploads/", verbose_name="Файл")
    material = models.ForeignKey(
        Material,
        related_name="attachments",
        verbose_name="К какому материалу",
        on_delete=models.CASCADE,
    )
    file_type = models.ForeignKey(
        AttachmentType,
        related_name="attachment_type",
        verbose_name="Тип прикрепления",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Прикрипление"
        verbose_name_plural = "Прикрепления"
        
    def __str__(self):
        return self.name
