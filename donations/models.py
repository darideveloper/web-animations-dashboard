from django.db import models
from django.utils import timezone

class Mosaic (models.Model):
    id = models.AutoField(primary_key=True)
    donor = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='mosaic')
    
    def __str__ (self):
        return self.donor
    
    class Meta:
        verbose_name = 'Mosaic donor'
        verbose_name_plural = 'Mosaic donors'
        
class ScreenLeaves (models.Model):
    id = models.AutoField(primary_key=True)
    donor_frirst_name = models.CharField(max_length=100)
    donor_last_name = models.CharField(max_length=100, blank=True, default='')
    
    def __str__ (self):
        return f"{self.donor_frirst_name} {self.donor_last_name}"
    
    class Meta:
        verbose_name = 'Screen leaves donor'
        verbose_name_plural = 'Screen leaves donors'
        
class ChristmasLandingPage (models.Model):
    
    SIZES = [
        ("s", "small"),
        ("m", "medium"),
        ("l", "large")
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='christmas_landing_page')
    size = models.CharField(
        max_length=1,
        choices=SIZES,
        default="s"
    )
    
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name = 'Christmas landing page donor'
        verbose_name_plural = 'Christmas landing page donors'

class CatDog (models.Model):
    
    ANIMALS = [
        ("cat", "cat"),
        ("dog", "dog"),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    team = models.CharField(
        max_length=3,
        choices=ANIMALS,
        default="cat"
    )
    
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name = 'Cat Dog donor'
        verbose_name_plural = 'Cat Dog donors'
        
class Setting (models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    datetime = models.DateTimeField(blank=True, null=True, default=timezone.now)
    enabled = models.BooleanField(default=False)
    value = models.CharField(max_length=100, blank=True, null=True, default='')
    
    def __str__ (self):
        data = []
        if self.datetime:
            data.append(f"{self.datetime}")
        if self.enabled:
            data.append(f"{self.enabled}")
        if self.value:
            data.append(f"{self.value}")
            
        return f"{self.name} ({' - '.join(data)})"
    
class Pinata (models.Model):
    TEAMS = [
        ("team1", "TEAM 1"),
        ("team2", "TEAM 2"),
        ("team3", "TEAM 3"),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField(default=0)
    team = models.CharField(
        max_length=5,
        choices=TEAMS,
        default="cat"
    )
    
    def __str__ (self):
        return f"{self.name} ({self.amount})" 
        
        