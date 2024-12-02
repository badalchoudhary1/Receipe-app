 

from django.urls import path
from . import views



urlpatterns = [
    path('receipes/', views.receipes, name="receipes"),  # Matches /receipes/
    path('delete/<int:id>/', views.delete_receipe, name="delete_receipe"), 
    path('update/<int:id>/', views.update_receipe, name="update_receipe"), 
]