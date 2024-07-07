from typing import Any
from django.core.management.base import BaseCommand, CommandError
from tests.models import *


class Command(BaseCommand):
    help = "Load base test"

    def handle(self, *args: Any, **options: Any) -> str | None:
        themes = seed_themes()
        seed_tests(themes)


def seed_tests(themes: list):
    pass

def seed_themes() -> list:
    theme1 = Theme.objects.create(title="Поражающие факторы источников чрезвычайных ситуаций, характерных для мест расположения и производственной деятельности организации, а также оружия массового поражения и других видов оружия.")
    theme2 = Theme.objects.create(title="Порядок получения сигнала 'ВНИМАНИЕ ВСЕМ!' с информацией о воздушной тревоге, химической тревоге, радиационной опасности или угрозе катастрофического затопления и действий работников организации по ним.")
    theme3 = Theme.objects.create(title="Порядок и правила использования средств индивидуальной и коллективной защиты, а также средств пожаротушения, имеющихся в организации.")
    theme4 = Theme.objects.create(title="Действия работников при аварии, катастрофе и пожаре на территории организации.")
    theme5 = Theme.objects.create(title="Действия работников организации при угрозе и возникновении чрезвычайных ситуаций и военных конфликтов")
    theme6 = Theme.objects.create(title="Оказание первой помощи.")
    theme7 = Theme.objects.create(title="Действия работников организации в условиях негативных и опасных факторов бытового характера.")
    
    return [theme1, theme2, theme3, theme4, theme5, theme6, theme7]