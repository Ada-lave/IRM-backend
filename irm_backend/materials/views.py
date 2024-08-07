from rest_framework import views
from .serializers import MaterialREADSerializer, AttachmentSerializer, ThemeSerializer
from .models import Material, Attachment, Theme
from rest_framework.response import Response

class MaterialViewSet(views.APIView):
    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialREADSerializer(materials, many=True)
        
        return Response(serializer.data)

class MaterialDetailViewSet(views.APIView):
    def get(self, request, pk):
        material = Material.objects.get(pk=pk)
        material_serializer = MaterialREADSerializer(material)
        
        attachments = material.attachments.all()
        attachment_serializer = AttachmentSerializer(attachments, many=True)
        
        response = material_serializer.data
        response["attachments"] = attachment_serializer.data
        return Response(response)
    
class ThemeViewSet(views.APIView):
    def get(self, request):
        themes = Theme.objects.all()
        theme_serializer = ThemeSerializer(themes, many=True)
        
        return Response(theme_serializer.data)

class ThemeDetailViewSet(views.APIView):
    def get(self, request, pk):
        
        try:
            theme = Theme.objects.get(pk=pk)
            theme_serializer = ThemeSerializer(theme)            
            return Response(theme_serializer.data)
        except Theme.DoesNotExist:
            return Response({"detail": "data not found"}, status=404)

    
