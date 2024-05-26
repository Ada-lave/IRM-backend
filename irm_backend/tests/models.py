from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Темы к тестированию"
        verbose_name_plural = "Темы к тестированию"

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    theme = models.ForeignKey(Theme, verbose_name="Тема", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    test = models.ForeignKey(
        Test,
        related_name="questions",
        verbose_name="Тест",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.TextField(verbose_name="Содержимое ответа", blank=False)
    is_right = models.BooleanField(default=False, verbose_name="Правильный ли ответ?")
    question = models.ForeignKey(
        Question,
        verbose_name="Вопрос",
        on_delete=models.CASCADE,
        related_name="answers",
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.title[:100]


class Meterial(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title[:100]

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        


# Таблицы для проверки тестов

class TestUser(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class TestUserQuestion(models.Model):
    question = models.ForeignKey(TestUser, on_delete=models.CASCADE)