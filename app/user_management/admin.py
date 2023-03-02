from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "staff_id",
        "fullname",
        "gender",
        "email",
        "pc_id",
        "ip_address",
        "is_active",
    ]
    list_display_links = ["staff_id", "fullname"]
