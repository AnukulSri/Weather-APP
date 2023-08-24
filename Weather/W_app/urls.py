from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home),
    path('',views.static),
    path('display',views.display),
    path('discard/<str:roll>',views.discard),
    path('edit/<str:roll>',views.edit),
    path('update/<str:roll>',views.update)
]