from django.contrib import admin
from accounts.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_superuser", "last_login"]
    list_filter = ["is_superuser"]
    search_fields = ["email", "username"]
    ordering = ["last_login"]
