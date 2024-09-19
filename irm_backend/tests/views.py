from rest_framework import generics, views
from .models import Test, Answer
from rest_framework.response import Response
from .serializers import TestSerializer, ResultSerializer



class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

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
            