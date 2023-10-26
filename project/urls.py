from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('',include('home.urls')),
    path('login/',include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('train/',include('trains.urls'))
]
