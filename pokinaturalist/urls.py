from django.urls import path
from . import views
from .views import SignUp

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
]
