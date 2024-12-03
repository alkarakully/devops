from django.shortcuts import render
from django.http import HttpResponse
import socket
from django.template import loader

# Create your views here.


def get_hostname(request):
    hostname = socket.gethostname()
    hosts = {"hostname": hostname}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))