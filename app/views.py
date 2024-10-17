from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def hey_you_view(request: HttpRequest, name) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def how_old_view(request: HttpRequest, end, birthyear) -> HttpResponse:
    return HttpResponse({end - birthyear})


def order_view(request: HttpRequest, burgers, fries, drinks) -> HttpResponse:
    return HttpResponse("{:.2f}".format(((burgers * 4.5) + (fries * 1.5) + drinks)))
