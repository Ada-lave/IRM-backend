from rest_framework import serializers
from .models import *


class AttachmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentType
        fields = "__all__"


class AttachmentSerializer(serializers.ModelSerializer):
    file_type = AttachmentTypeSerializer(read_only=True)

    class Meta:
        model = Attachment
        fields = ("name", "path", "theme_id", "file_type")


class MaterialREADSerializer(serializers.ModelSerializer):
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


class ThemeSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Theme
        fields = ("title", "attachments")


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "fio", "gender", "department_id")


class DepartmentSerializer(serializers.ModelSerializer):
    # employes = EmployeeSerializer(many=True)

    class Meta:
        model = Department
        fields = ("id", "title",)
