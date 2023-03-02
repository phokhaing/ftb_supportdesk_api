from django.contrib import admin
from .models import DepartmentModel


@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name_en',
                    'name_kh',
                    'description',
                    'is_active']

    list_display_links = ["id", "name_en", "name_kh"]
