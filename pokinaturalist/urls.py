from django.urls import path, include
from . import views
from .views import HomePageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', views.index, name='pokinaturalist'),
]
