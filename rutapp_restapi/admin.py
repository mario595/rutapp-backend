from django.contrib import admin

from rutapp_restapi.models import Walk


@admin.register(Walk)
class WalkAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'region', 'length')
