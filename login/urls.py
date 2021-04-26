from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('accounts/login/', views.accounts_login, name='account_login'),
    path('accounts/signup/', views.accounts_signup, name='account_signup'),
]
