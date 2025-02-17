from django.shortcuts import render
from geoapp.models import Location

def location_list(request):
    # Récupérer toutes les localisations
    locations = Location.objects.all()
    # Passer les localisations au template
    return render(request, 'geoapp/location_list.html', {'locations': locations})