from django.contrib import admin
from .models import *

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
# Register your models here.
