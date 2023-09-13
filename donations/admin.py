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
    
@admin.register(models.ChristmasLandingPage)
class ChristmasLandingPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'size')
    list_per_page = 50
    search_fields = ('name',)
    ordering = ('name',)
    
@admin.register(models.CatDog)
class CatDogAdmin (admin.ModelAdmin):
    list_display = ('name', 'amount', 'team')
    list_per_page = 50
    search_fields = ('name', 'amount')
    ordering = ('name', 'amount')
    
@admin.register(models.Setting)
class SettingAdmin (admin.ModelAdmin):
    list_display = ('name', 'datetime', 'enabled', 'value')
    list_per_page = 50
    search_fields = ('name', 'datetime', 'enabled', 'value')
    ordering = ('name', 'datetime', 'enabled', 'value')

@admin.register(models.Pinata)
class PinataAdmin (admin.ModelAdmin):
    list_display = ('name', 'amount', 'team')
    list_per_page = 50
    search_fields = ('name', 'amount')
    ordering = ('name', 'amount')
    list_filter = ('team',)
    
@admin.register(models.PinataTeam)
class PinataTeamAdmin (admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 50
    ordering = ('name',)
    
# @admin.register(models.BitStar