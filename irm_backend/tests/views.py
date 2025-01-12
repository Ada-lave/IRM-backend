from rest_framework import generics, views
from .models import Test, Answer, Result
from rest_framework.response import Response
from .serializers import TestSerializer, ResultSerializer
from urllib.parse import quote
from django.http import HttpResponse
from utils.exporter import Export
import datetime
class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class ResultView(views.APIView):
    def get(self, request):
        results = Result.objects.all()
        test_id = request.query_params.get("test_id")
        department_id = request.query_params.get("department_id")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        if test_id:
            results = results.filter(test_id=test_id)

        if department_id:
            results = results.filter(user__department_id=department_id)

        if start_date:
            start_date = datetime.date.fromtimestamp(int(start_date))
            results = results.filter(compleated_at__gte=start_date)

        if end_date:
            end_date = datetime.date.fromtimestamp(int(end_date))
            results = results.filter(compleated_at__lte=end_date)

        result_serializer = ResultSerializer(results, many=True)

        return Response(result_serializer.data)


class ResultExportView(views.APIView):
    def get(self, request):
        exporter = Export()
        workbook = exporter.export(
            test_id=request.query_params.get("test_id"),
            department_id=request.query_params.get("department_id"),
        )
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        filename = "Отчет по тестированию.xlsx"
        response["Content-Disposition"] = (
            f"attachment; filename*=UTF-8''{quote(filename)}"
        )

        # Запрещаем кэширование
        response["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response["Pragma"] = "no-cache"
        response["Expires"] = "0"

        workbook.save(response)

        return response


class TestCheckView(views.APIView):

    def post(self, request, pk):
        data = dict(request.data)
        test = Test.objects.get(id=data.get("id"))
        total = 0
        score = 0
        result = Result.objects.filter(test_id=test.id, user_id=data.get("employee_id"))
        
        if result.exists():  
            result.delete()

        for question in data["questions"]:
            total += 1
            for answer in question["answers"]:
                if (
                    Answer.objects.get(
                        id=answer["id"], question_id=question["id"]
                    ).is_right is True
                ):
                    score += 1

        result_serializer = ResultSerializer(
            data={
                "total": total,
                "score": score,
                "test": data.get("id"),
                "user": data.get("employee_id"),
            }
        )
        result_serializer.is_valid(raise_exception=True)
        result_serializer.save()

        # data = dict(request.data.get("questions"))
        return Response(result_serializer.data)
