from django.conf.urls import url
from . import views


urlpatterns=[
   
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^images',views.images,name ='images')

]
