# from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from django.contrib.auth.forms import UserCreationForm                                          
from django import forms                                                                          
from django.urls import reverse_lazy                                                                
from django.views import generic

"""
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import CreateUser
from ipware import get_client_ip

from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
"""
# Create your views here.
def index(request):
    client_ip = get_user_ip_addr(request)
    if client_ip is None:
        raise exceptions.FieldDoesNotExist("Client IP address is missing from request.")

    request.session["IPv4_ADDR"] = client_ip
    return HttpResponse(f"Client IP addr: {client_ip}")


def get_user_ip_addr(request):
    client_ip, _ = get_client_ip(request)
    return client_ip

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

"""    
class CreateUser(forms.ModelForm):
    
    A form that creates a user, with no privileges, from the given username and
    password.
    
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        entry = CreateUser(NAME=User.username, PASSWORD=User.password)

        #        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        entry = CreateUser(NAME=user.get_username(), PASSWORD=self.cleaned_data["password1"])
        entry.save()
        
        if commit:
            user.save()
        return user
"""
