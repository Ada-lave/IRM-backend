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
    list_display = ("name", "path", "file_type", "theme", "section")
    fields = ("path", "file_type", "theme", "section")


@admin.register(AttachmentType)
class FileTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["fio"]
    list_display = ["fio", "department", "gender"]
    list_filter = ["department"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ["title"]



# Register your models here.
