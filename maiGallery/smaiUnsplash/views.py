from django.shortcuts import render
# from .models import Category, Image, Location


# Create your views here.
def home(request):
    title = "Sami-Mai Unsplash"
    return render(request, 'index.html', {"title": title})
