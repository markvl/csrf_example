from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.SimpleFormView.as_view(), name='simple_form'),
]
