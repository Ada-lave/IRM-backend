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
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Тип прикрепления"
        verbose_name_plural = "Тип прикреплений"

    def __str__(self):
        return self.type

class Section(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя раздела')
    url = models.URLField(verbose_name="Ссылка на раздел", blank=True)
    
    class Meta:
        verbose_name = "Раздел сайта"
        verbose_name_plural = "Разделы сайта"
    
    def __str__(self):
        return self.name
        
class Attachment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя файла")
    path = models.FileField(upload_to="static/uploads/", verbose_name="Файл")
    theme = models.ForeignKey(
        Theme,
        related_name="attachments",
        verbose_name="К какому материалу",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    file_type = models.ForeignKey(
        AttachmentType,
        related_name="attachment_type",
        verbose_name="Тип прикрепления",
        on_delete=models.CASCADE,
    )
    section = models.ForeignKey(
        Section, 
        related_name="attachments", 
        verbose_name="К какому разделу сайта", 
        on_delete=models.CASCADE,
        blank=True,
        null=True
        )
    
    def save(self, *args, **kwargs):
        if not self.name and self.path:
            self.name = self.path.name
        
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Прикрипление"
        verbose_name_plural = "Прикрепления"

    def __str__(self):
        return self.name