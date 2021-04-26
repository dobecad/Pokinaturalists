from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from django.views.generic import TemplateView

import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def login(request):
    context = {}
    template_base_dir = 'login/'
    template_to_return = f'{template_base_dir}/index.html'
    return (request, f'{template_to_return}', context)