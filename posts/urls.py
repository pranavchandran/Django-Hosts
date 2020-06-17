from django.urls import path
from phosts.views import home
from django.contrib import admin

from posts.views import (
    post_list,
    post_detail,
    )

app_name = 'posts'  

# urlpatterns = [
#     url(r'^$', post_list, name='list'),
#     url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
# ]

urlpatterns = [
    # path('admin', admin.site.urls),
    path('',post_list, name='list'),
    path('<slug:slug>/',post_detail, name='detail'),


]