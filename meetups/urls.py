from django.urls import path
from . import views

urlpatterns = [
    path('meetups', views.index) #for example the url will be==> ourdomain.com/meetsup
]