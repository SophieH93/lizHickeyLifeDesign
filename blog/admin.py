from django.contrib import admin
from . import models

# Registers blog models in admin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')


admin.site.register(models.Post, AuthorAdmin)