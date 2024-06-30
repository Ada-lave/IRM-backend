from rest_framework.serializers import ModelSerializer
from .models import Material

class MaterialREADSerializer(ModelSerializer):
    read_only = True
    class Meta:
        model = Material
        fields = ("id", "title", "text")