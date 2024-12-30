from django.shortcuts import render, redirect
from .models import Reciepe
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# User Registration view

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

# Profile view - protected with login_required
@login_required
def profile(request):
    return render(request, 'profile.html')



# View for displaying all recipes and the search functionality
@login_required
def receipes(request):
    queryset = Reciepe.objects.all()

    # Search functionality
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context = {'receipes': queryset}
    return render(request, "receipes.html", context)

# View for adding a new recipe
@login_required
def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # Create new recipe
        Reciepe.objects.create(receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image)
        return redirect('receipes')  # Redirect to the recipes page after adding the recipe

    return render(request, "add_recipe.html")

# View for deleting a recipe
@login_required
def delete_receipe(request, id):
    receipe = Reciepe.objects.get(id=id)
    receipe.delete()
    return redirect('receipes')

# View for updating a recipe
@login_required
def update_receipe(request, id):
    receipe = Reciepe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description

        if receipe_image:
            receipe.receipe_image = receipe_image

        receipe.save()
        return redirect('receipes')

    context = {'receipe': receipe}
    return render(request, "update_receipe.html", context)

