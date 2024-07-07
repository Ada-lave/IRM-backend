from django.contrib import admin
from .models import *

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass

@admin.register(AttachmentType)
class FileTypeAdmin(admin.ModelAdmin):
    pass
# Register your models here.
