from donations import models
from django.http import JsonResponse, HttpResponse

def home (request):
    
    # Return full donations model
    message = "running"
    return HttpResponse(message)

def get_donations_mosaic(request):
    
    # Return full donations model
    donations = models.Mosaic.objects.all()
    return JsonResponse(list(donations.values()), safe=False)