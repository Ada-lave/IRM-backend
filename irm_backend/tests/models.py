from django.db import models
from django.contrib.auth.models import User

from materials.models import Theme, Employee

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
        verbose_name = "Вопрос к тесту"
        verbose_name_plural = "Вопросы к тестам"

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
        verbose_name = "Ответы к вопросам"
        verbose_name_plural = "Ответы к вопросам"

    def __str__(self):
        return self.title[:100]


# Таблицы для проверки тестов


class Result(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тестирование')
    score = models.IntegerField(verbose_name='Правильных')
    total = models.IntegerField(verbose_name='Всего вопросов')

    class Meta:
        verbose_name = "Результат тестирования"
        verbose_name_plural = "Результаты тестирования"
