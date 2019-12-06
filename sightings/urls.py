from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('map/', views.map),
    path('sightings/', views.sightings),
    path('add/', views.add_sq),
    path('sightings/<str:UID>/', views.edit_sq),
    path('sightings/stats', views.stats),
]
