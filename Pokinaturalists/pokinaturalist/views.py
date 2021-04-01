from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions

from ipware import get_client_ip

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