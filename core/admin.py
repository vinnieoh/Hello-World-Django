from django.contrib import admin

from .models import UsuarioModel

@admin.register(UsuarioModel)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')