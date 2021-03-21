from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Query, Replies
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email',]

admin.site.register(User, CustomUserAdmin)
