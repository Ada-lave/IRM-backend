from rest_framework import views
from .serializers import MaterialREADSerializer, AttachmentSerializer
from .models import Material, Attachment
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
    
