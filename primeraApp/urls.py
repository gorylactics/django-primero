from django.urls import path
from . import views

urlpatterns = [
    path('' , views.root),
    path('blogs/' , views.index),
    path('blogs/news/' , views.new),
    path('blogs/create/' , views.create),
    path('blogs/<int:numero>', views.show),
    path('blogs/<int:numero>/edit', views.edit ),
    path('blogs/<int:numero>/delete' , views.destroy),
    path('blogs/json' , views.json)
]
