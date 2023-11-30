from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

def hello_view(request, name):
    if not name:
        return HttpResponseNotFound("Please provide a valid name.")
    elif name == '':
        return HttpResponseNotFound("Please provide a valid name in the URL.")
    return HttpResponse(f"Hello, {name}!")
def noname_view(request):
    return HttpResponseNotFound("Please provide a valid name.")
