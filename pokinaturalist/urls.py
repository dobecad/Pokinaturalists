from django.urls import path
from . import views

urlpatterns = [
    # path('home/', HomePageView.as_view(), name='home'),
    path('', views.index, name='index'),
    path('', views.index, name='pokinaturalist')
]
