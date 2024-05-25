from rest_framework import generics
from .models import Test
from .serializers import TestSerializer



class TestView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer