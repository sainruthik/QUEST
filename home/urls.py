from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('historical',views.historical,name='historical'),
    path('temples',views.temples,name='temples'),
    path('parks',views.parks,name='parks'),
    path('cities',views.cities,name='cities'),
    path('beaches',views.beaches,name='beaches'),
    path('hills',views.hills,name='hills'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('blog',views.blog,name='blog'),
    re_path('states/[0-9]+',views.places,name='states'),
    re_path('categories/[a-zA-Z]+',views.places,name='states'),
    re_path('place/[a-zA-Z]+',views.place,name='place')
]