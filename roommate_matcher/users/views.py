from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomLoginForm, CompatibilityForm
from .models import CompatibilityProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('compatibility') 
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    return render(request, 'users/dashboard.html')


@login_required
def compatibility_form_view(request):
    profile = None
    try:
        profile = CompatibilityProfile.objects.get(user=request.user)
    except CompatibilityProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = CompatibilityForm(request.POST, instance=profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Your compatibility profile has been saved successfully!")  # ✅ Success message
    else:
        form = CompatibilityForm(instance=profile)

    return render(request, 'users/compatibility_form.html', {'form': form})
