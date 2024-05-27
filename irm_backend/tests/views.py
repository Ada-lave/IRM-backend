from rest_framework import generics, views
from .models import Test, Result, Question, Answer
from rest_framework.response import Response
from .serializers import TestSerializer, QuestionSerializer, AnswerSerializer
from django.http import HttpRequest
import json


class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestCheckView(views.APIView):
    
    def post(self, request, pk):
        print(type(request.data), request.data)
        # result = Result()
        # test_id = request.data.get("id")
        # data = dict(request.data)
        
        # for question in data["questions"]:
        #     print(type(question))
        #     for answer in question["answers"]:
        #         result.total += 1
        #         if Answer.objects.get(id=answer["id"],question_id=question["id"]):
        #             result.score += 1
        # result.test = Test.objects.get(id=test_id)
        # result.save()
                    
        # data = dict(request.data.get("questions"))
        return Response({"score": 10})
            