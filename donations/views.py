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

def get_donations_screen_leaves(request):
    
    # Return full donations model
    donations = models.ScreenLeaves.objects.all()
    return JsonResponse(list(donations.values()), safe=False)

def get_donations_christmas_landing_page(request):
    
    # Return full donations model
    donations = models.ChristmasLandingPage.objects.all()
    return JsonResponse(list(donations.values()), safe=False)

def get_donations_cat_dog (request):
    
    # Return full donations model
    donations = models.CatDog.objects.all()
    return JsonResponse(list(donations.values()), safe=False)
