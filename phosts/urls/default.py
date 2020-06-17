from django.contrib import admin
from django.urls import path,include
from phosts.views import home
urlpatterns = [
    path('admin', admin.site.urls),
    
    path('',home, name='home'),
    path('posts/',include('posts.urls',namespace='posts')),



]