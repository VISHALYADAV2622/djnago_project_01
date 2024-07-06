from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


"""
to render template 
"""

def home(repuest):
    return render (repuest,"home.html")

def about(request):
    data= {
        'page':'about_page'
    }
    return render (request, "about.html",data)
