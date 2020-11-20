from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('stockMarket.urls')),    #localhost:8000/
    path('admin/', admin.site.urls),
] 

