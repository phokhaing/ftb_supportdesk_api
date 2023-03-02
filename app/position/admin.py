from django.contrib import admin
from .models import PositionModel


@admin.register(PositionModel)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name_en',
                    'name_kh',
                    'description',
                    'is_active']

    list_display_links = ["id", "name_en", "name_kh"]
