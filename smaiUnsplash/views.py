from django.http import Http404
from django.shortcuts import render
from .models import Category, Image


# Create your views here.
def home(request):
    images = Image.image_item()
    return render(request, 'index.html', {"images": images})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get('category')
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'albums/search.html', {"message": message, "categories": searched_images})

    else:
        message = "...You haven't searched for any term"
        return render(request, 'albums/search.html', {"message": message})
