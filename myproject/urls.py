from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geoapp/', include('geoapp.urls')),  # Inclure les URLs de geoapp
]