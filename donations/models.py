from django.db import models

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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='christmas_landing_page')
    
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name = 'Christmas landing page donor'
        verbose_name_plural = 'Christmas landing page donors'