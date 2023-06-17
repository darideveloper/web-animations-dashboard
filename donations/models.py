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
        
    