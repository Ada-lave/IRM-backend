import openpyxl
from tests.models import Result
import datetime

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
            row = [res.id, res.test.title, res.user.fio, res.total, res.score, res.compleated_at]
            worksheet.append(row)

        return workbook
