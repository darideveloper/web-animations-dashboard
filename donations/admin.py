from donations import models
from django.contrib import admin

@admin.register(models.Mosaic)
class MosaicAdmin(admin.ModelAdmin):
    list_display = ('donor', 'image')
    list_per_page = 50
    search_fields = ('donor',)
    ordering = ('donor',)