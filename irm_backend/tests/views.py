from rest_framework import generics, views
from .models import Test
from rest_framework.response import Response
from .serializers import TestSerializer
from django.http import HttpRequest



class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestCheckView(views.APIView):
    
    def post(self, request: HttpRequest, pk):
        test_serializer = TestSerializer(data=request.data)
        test_serializer.is_valid()
        
        print(test_serializer.validated_data)

        return Response(test_serializer.validated_data)
            