import openpyxl
from tests.models import Result
from zoneinfo import ZoneInfo
import time

class Export:

    def export(self, test_id=None, department_id=None) -> openpyxl.Workbook:
        results = Result.objects.all()
        if test_id:
            results = results.filter(test_id=test_id)

        if department_id:
            results = results.filter(user__department_id=department_id)

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Отчет по тестированию"
        columns = [
            "ID",
            "Тест",
            "Пользователь",
            "Всего вопросов",
            "Верных ответов",
            "Время прохождения"
        ]
        worksheet.append(columns)
        worksheet.column_dimensions['B'].width = 40
        worksheet.column_dimensions['C'].width = 35
        worksheet.column_dimensions['D'].width = 15
        worksheet.column_dimensions['E'].width = 15
        worksheet.column_dimensions['F'].width = 40


        for res in results:
            local_timezone = ZoneInfo(time.tzname[0])
            date = res.compleated_at.replace(tzinfo=local_timezone)
            row = [res.id, res.test.title, res.user.fio, res.total, res.score, date.strftime("%Y-%m-%d %H:%M:%S")]
            worksheet.append(row)

        return workbook
