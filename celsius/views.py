from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render


def index(request):
    return redirect('pro_index')
