from donations import models
from django.contrib import admin

@admin.register(models.Mosaic)
class MosaicAdmin(admin.ModelAdmin):
    list_display = ('donor', 'image')
    list_per_page = 50
    search_fields = ('donor',)
    ordering = ('donor',)
    
@admin.register(models.ScreenLeaves)
class ScreenLeavesAdmin(admin.ModelAdmin):
    list_display = ('donor_frirst_name', 'donor_last_name')
    list_per_page = 50
    search_fields = ('donor_frirst_name', 'donor_last_name')
    ordering = ('donor_frirst_name','donor_last_name')