  
from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import include, path

def about(request):
    return render(request,'website/about.html')
def home(request):
    return render(request,'website/home.html')