from django.shortcuts import render
from django.http import HttpResponse
import socket, os
from django.template import loader

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    with open("/opt/custom_header", "r") as header_file:
        custome_header = header_file.readlines()[0]
    hosts = {"hostname": hostname, "custom_header": custome_header}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))

def members(request):
    hostname = socket.gethostname()
    with open("/opt/custom_header", "r") as header_file:
        custome_header = header_file.readlines()[0]
    hosts = {"hostname": hostname, "custom_header": custome_header}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))