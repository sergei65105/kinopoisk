from django.contrib import admin

from core.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_editable = ('avatar',)
    list_display = (
        'id',
        'username',
        'avatar',
        'is_staff',
    )
