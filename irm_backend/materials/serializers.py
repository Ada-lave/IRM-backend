from rest_framework.serializers import ModelSerializer
from .models import Material, Attachment, Theme, AttachmentType


class AttachmentTypeSerializer(ModelSerializer):
    class Meta:
        model = AttachmentType
        fields = "__all__"


class AttachmentSerializer(ModelSerializer):
    file_type = AttachmentTypeSerializer(read_only=True)

    class Meta:
        model = Attachment
        fields = ("name", "path", "theme_id", "file_type")


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


class ThemeSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Theme
        fields = ("title", "attachments")
