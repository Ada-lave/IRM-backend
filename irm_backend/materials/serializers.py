from rest_framework.serializers import ModelSerializer
from .models import Material, Attachment


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"


class MaterialREADSerializer(ModelSerializer):
    read_only = True
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        fields = (
            "id",
            "title",
            "text",
            "attachments",
        )
