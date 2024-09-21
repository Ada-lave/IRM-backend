from rest_framework import generics, views
from .models import Test, Answer, Result
from rest_framework.response import Response
from .serializers import TestSerializer, ResultSerializer
import openpyxl
from urllib.parse import quote
from django.http import HttpResponse

class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class ResultView(views.APIView):
    def get(self, request):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Отчет по тестированию'
        columns = ['ID', 'Тест', 'Пользователь', 'Всего вопросов', 'Верных ответов']  # Замените на свои поля
        worksheet.append(columns)
        
        data = Result.objects.all()
        
        for res in data:
            row = [res.id, res.test.title, res.user.fio, res.total, res.score]
            worksheet.append(row)
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        filename = 'Отчет по тестированию.xlsx'
        response['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{quote(filename)}'

        # Запрещаем кэширование
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        workbook.save(response) 
        
        return response
        

class TestCheckView(views.APIView):
    
    def post(self, request, pk):
        data = dict(request.data)
        test = Test.objects.get(id=data.get("id"))
        total = 0
        score = 0
        for question in data["questions"]:
            total += 1
            for answer in question["answers"]:
                if Answer.objects.get(id=answer["id"], question_id=question["id"]).is_right == True :
                    score += 1
        
        result_serializer = ResultSerializer(data={"total": total, "score": score, "test": test.id, "user": request.user.id})
        result_serializer.is_valid(raise_exception=True)
        result_serializer.save()
        
        
                    
        # data = dict(request.data.get("questions"))
        return Response(result_serializer.data)
            