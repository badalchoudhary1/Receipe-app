 

from django.urls import path
from . import views



urlpatterns = [
    path('receipes/', views.receipes, name="receipes"),  # Matches /receipes/
    path('delete/<int:id>/', views.delete_receipe, name="delete_receipe"), 
    path('update/<int:id>/', views.update_receipe, name="update_receipe"), 
    path('add_recipe/', views.add_recipe, name="add_recipe"), 
     path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]