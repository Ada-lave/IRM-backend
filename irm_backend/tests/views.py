from rest_framework import generics, views
from .models import Test
from rest_framework.response import Response
from .serializers import TestSerializer




class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestCheckView(views.APIView):
    
    def post(self, request, pk):
        return Response("HI")