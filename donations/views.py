from donations import models
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

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
    donations_list = list(donations.values())
    
    # Get enabled from settings
    now = timezone.now().astimezone()
    enabled_found = models.Setting.objects.filter(name="CatDog", datetime__gte=now, enabled=True)
    enabled = False
    if enabled_found:
        enabled = True
        
    # retu5n data
    return JsonResponse({
        "donations": donations_list,
        "enabled": enabled,
    }, safe=False)

def pinata (request): 
    
    # Return full donations model
    donations = models.Pinata.objects.all()
    donations_list = list(donations.values())
    
    # Add team name
    teams = models.PinataTeam.objects.all()
    
    for donation in donations_list:
        donation["team"] = teams.get(id=donation["team_id"]).name
    
    # retu5n data
    return JsonResponse({
        "donations": donations_list,
    }, safe=False)