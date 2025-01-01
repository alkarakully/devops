from django.shortcuts import render
from django.http import HttpResponse
import socket, os
from django.template import loader

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    file_path = "/opt/custom_header"
    default_content = "This is the default header content\n"
    if not os.path.exists(file_path):
        # If the file does not exist, create it and write the default content
        with open(file_path, "w") as header_file:
            header_file.write(default_content)
            
    with open("/opt/custom_header", "r") as header_file:
        custome_header = header_file.readlines()[0]
    hosts = {"hostname": hostname, "custom_header": custome_header}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))

def members(request):
    hostname = socket.gethostname()
    file_path = "/opt/custom_header"
    default_content = "This is the default header content\n"
    if not os.path.exists(file_path):
        # If the file does not exist, create it and write the default content
        with open(file_path, "w") as header_file:
            header_file.write(default_content)

    with open("/opt/custom_header", "r") as header_file:
        custome_header = header_file.readlines()[0]
    hosts = {"hostname": hostname, "custom_header": custome_header}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(hosts))