from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions

from ipware import get_client_ip

import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def index(request):
    client_ip = get_user_ip_addr(request)
    if client_ip is None:
        raise exceptions.FieldDoesNotExist("Client IP address is missing from request.")

    request.session["IPv4_ADDR"] = client_ip
    context = {
        "mapboxAppToken": str(os.getenv('MapboxAppToken'))
    }
    template_base_dir = 'pokinaturalist/game'
    template_to_return = f'{template_base_dir}/geo.html'
    return render(request, f'{template_to_return}', context)


def get_user_ip_addr(request):
    client_ip, _ = get_client_ip(request)
    return client_ip