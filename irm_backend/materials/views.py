from rest_framework import views
from .serializers import MaterialREADSerializer
from .models import Material
from rest_framework.response import Response

class MaterialViewSet(views.APIView):
    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialREADSerializer(materials, many=True)
        
        return Response(serializer.data)

class MaterialDetailViewSet(views.APIView):
    def get(self, request, pk):
        material = Material.objects.get(pk=pk)
        serializer = MaterialREADSerializer(material)
        
        return Response(serializer.data)
    
