from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    search_fields = ["title"]



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "view_test_link")
    search_fields = ["title"]
    list_filter = ["test"]

    def view_test_link(self, obj):
        url = (
            reverse("admin:tests_test_changelist")
            + "?"
            + urlencode({"questions__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Перейти к тесту</a>', url)

    view_test_link.short_description = "Тест"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_right", "view_q_link")
    search_fields = ["title"]
    list_filter = ["question__test", "question"]


    def view_q_link(self, obj):
        url = (
            reverse("admin:tests_question_changelist")
            + "?"
            + urlencode({"answers__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Перейти к вопросу</a>', url)

    view_q_link.short_description = "Вопрос"


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass
