from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('about/',include('home.urls')),
    path('resources/',include('home.urls')),
    path('page1/',include('home.urls')),
    path('page2/',include('home.urls'))
]