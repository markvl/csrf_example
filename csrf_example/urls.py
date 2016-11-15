from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'post_to_me/', include('post.urls')),
]
