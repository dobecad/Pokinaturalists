from django.urls import path, include
from . import views
from .views import HomePageView

urlpatterns = [
<<<<<<< HEAD
    path('home/', HomePageView.as_view(), name='home'),
    path('', views.index, name='index'),
=======
    path('', views.index, name='pokinaturalist')
>>>>>>> e1b5bc64838ab1a4e62d68acd0692e951e10e7ad
]
