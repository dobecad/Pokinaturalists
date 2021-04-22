from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', views.index, name='pokinaturalist'),
    path('shop', views.shop, name='shop'),
    path('items', views.items, name='items'),
    path('party', views.party, name='party'),
    path('profile', views.profile, name='profile'),
    path('friends', views.friends, name='friends')
]
