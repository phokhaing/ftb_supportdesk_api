from django.contrib import admin
from .models import BranchModel


@admin.register(BranchModel)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name_en',
                    'name_kh',
                    'address_en',
                    'is_active']

    list_display_links = ["id", "name_en", "name_kh"]
