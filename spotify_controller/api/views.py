from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Write our endpoints here.


def main(request):
    return HttpResponse("Hello World")
