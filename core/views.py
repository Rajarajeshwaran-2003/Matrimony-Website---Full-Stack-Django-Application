# views.py

from django.shortcuts import render, redirect
from .forms import CandidateForm, TestimonyForm, RegisterForm
from .models import Candidate, Testimony
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # To display error/success messages

def index(request):
    candidates = Candidate.objects.all()
    testimonies = Testimony.objects.all()
    return render(request, 'core/index.html', {
        'candidates': candidates,
        'testimonies': testimonies,
    })


def index(request):
    return render(request, 'core/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add first/last name to user model
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

def candidates(request):
    all_candidates = Candidate.objects.all()
    return render(request, 'core/candidates.html', {'candidates': all_candidates})

# ✅ Testimony view (no login required)
def testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimony submitted successfully.")
            return redirect('testimony')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TestimonyForm()
    all_testimonies = Testimony.objects.all()
    return render(request, 'core/testimony.html', {'form': form, 'testimonies': all_testimonies})


@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)  # Don't forget request.FILES
        if form.is_valid():
            form.save()
            return redirect('candidates')
    else:
        form = CandidateForm()
    return render(request, 'core/add_candidate.html', {'form': form})


def contact(request):
    return render(request, 'core/contact.html')
