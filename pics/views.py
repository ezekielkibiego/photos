import datetime as dt
from django.http  import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from .models import Images
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    Image = Images.objects.all()
    ctx = {'Image':Image}
    return render(request, 'all-pics/index.html', ctx)

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

def images(request,images_id):
    try:
        images = Images.objects.get(id = images_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pics/images.html", {"images":images})