from django.shortcuts import render
from django.http import HttpResponse
import socket, os
from django.template import loader

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    custome_header = os.environ.get("custom_header")
    hosts = {"hostname": hostname, "custom_header": custome_header}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))

def members(request):
    hostname = socket.gethostname()
    custome_header = os.environ("custom_header")
    hosts = {"hostname": hostname, "custom_header": custome_header}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))