import datetime as dt
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Images

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')



def index(request):
    Image = Images.objects.all()
    ctx = {'Image':Image}
    return render(request, 'all-pics/index.html', ctx)