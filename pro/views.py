from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from pro import models as m



def index(request):
    # if 'username' in request.POST and 'password' in request.POST:
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('internal')
    else:
        rv = {'next': '/pro/internal/'}
        return render(request, 'login.html', rv)


def internal(request):
    if request.user.is_authenticated:
        stations = m.Station.objects.all()
        rv = {'stations': [station.name.strip() for station in stations]}
        return render(request, 'internal.html', rv)
    else:
        stations = m.Station.objects.all()
        rv = {'stations': [station.name for station in stations]}
        return render(request, 'internal.html', rv)
        # return redirect('pro_index')
    
