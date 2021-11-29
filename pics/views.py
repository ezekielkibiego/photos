import datetime as dt
from django.http  import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from .models import Images,Location,Category
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    
    
    
    if 'category' in request.GET and request.GET["category"]:
        category_id = request.GET.get("category")
        Image = Images.objects.filter(category = category_id)
        
    elif 'location' in request.GET and request.GET["location"]:
        location_id = request.GET.get("location")
        Image = Images.objects.filter(location = location_id)
       
    else:
        Image = Images.objects.all()
            
    ctx = {'Image':Image, 'categories': categories, 'locations':locations }
    return render(request, 'all-pics/index.html',ctx)

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_category(search_term)
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

# def location(request, location_id):
#     locations = Location.objects.all()
#     images = Images.objects.filter(location_id=location_id)
#     location = Location.objects.get(id=location_id)
#     title = location
#     return render(request, "all-pics/images.html",{'images': images, 'locations': locations, 'title': title})

