from rest_framework.serializers import ModelSerializer
from .models import Material, Attachment



class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fileds = ("id","path")
        
class MaterialREADSerializer(ModelSerializer):
    read_only = True
    attachments = AttachmentSerializer(many=True)
    class Meta:
        model = Material
        fields = ("id", "title", "text", "attachments")