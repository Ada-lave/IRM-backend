from typing import Any
from django.core.management.base import BaseCommand, CommandError
from tests.models import *
from materials.models import *
import json
import os


class Command(BaseCommand):
    help = "Load base data"

    def handle(self, *args: Any, **options: Any) -> str | None:
        themes = seed_themes()
        seed_tests(themes)
        seed_videos(themes)
        seed_pdf_documents(themes)
        seed_sections()


def seed_tests(themes: list):
    with open("static/jsons/tests.json", encoding="utf-8") as f:
        tests = json.load(f)

    for test in tests["tests"]:
        created_test = Test.objects.create(title=test["name"], theme=themes[0])
        for question in test["questions"]:
            created_question = Question.objects.create(
                title=question["question"], test=created_test
            )
            for answer in question["options"]:
                created_answer = Answer.objects.create(
                    title=answer["answer"], question=created_question
                )


def seed_themes() -> list:
    theme1 = Theme.objects.create(
        title="Поражающие факторы источников чрезвычайных ситуаций, характерных для мест расположения и производственной деятельности организации, а также оружия массового поражения и других видов оружия."
    )
    theme2 = Theme.objects.create(
        title="Порядок получения сигнала 'ВНИМАНИЕ ВСЕМ!' с информацией о воздушной тревоге, химической тревоге, радиационной опасности или угрозе катастрофического затопления и действий работников организации по ним."
    )
    theme3 = Theme.objects.create(
        title="Порядок и правила использования средств индивидуальной и коллективной защиты, а также средств пожаротушения, имеющихся в организации."
    )
    theme4 = Theme.objects.create(
        title="Действия работников при аварии, катастрофе и пожаре на территории организации."
    )
    theme5 = Theme.objects.create(
        title="Действия работников организации при угрозе и возникновении чрезвычайных ситуаций и военных конфликтов"
    )
    theme6 = Theme.objects.create(title="Оказание первой помощи.")
    theme7 = Theme.objects.create(
        title="Действия работников организации в условиях негативных и опасных факторов бытового характера."
    )

    return [theme1, theme2, theme3, theme4, theme5, theme6, theme7]


def seed_videos(themes: list):
    video_type, _ = AttachmentType.objects.get_or_create(type="video")
    video_path = "static/videos"
    videos = os.listdir(video_path)
    for i in range(len(themes)):
        Attachment.objects.create(
            theme=themes[i],
            name=videos[i],
            path=f"{video_path}/{videos[i]}",
            file_type_id=video_type.id,
        )


def seed_pdf_documents(themes: list):
    pdf_document_type, _ = AttachmentType.objects.get_or_create(
        type="document/pdf"
    )
    pdfs_path = "static/pdfs"
    pdfs = os.listdir(pdfs_path)
    for i in range(len(themes)):
        attachment = Attachment.objects.create(
            theme=themes[i],
            name=pdfs[i],
            path=f"{pdfs_path}/{pdfs[i]}",
            file_type_id=pdf_document_type.id,
        )


def seed_sections():
    section_names = ["Инструктаж", "Документы", "Памятки"]
    for section_name in section_names:
        Section.objects.get_or_create(name=section_name)
