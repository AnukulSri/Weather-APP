from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('static',views.static),
    path('display',views.display)
]