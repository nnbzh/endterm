from django.contrib import admin

from app.sso.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
