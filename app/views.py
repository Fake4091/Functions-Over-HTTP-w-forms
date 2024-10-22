from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from app.forms import HeyForm, AgeForm, OrderForm

# Create your views here.


def hey_you_view(request: HttpRequest):
    form = HeyForm(request.GET)
    if form.is_valid():
        return render(
            request, "hey.html", {"form": form, "name": form.cleaned_data["name"]}
        )
    else:
        return render(request, "hey.html", {"form": form})


def how_old_view(request: HttpRequest):
    form = AgeForm(request.GET)
    if form.is_valid():
        return render(
            request,
            "age.html",
            {
                "form": form,
                "end": form.cleaned_data["end"],
                "birthyear": form.cleaned_data["birthyear"],
                "age": (form.cleaned_data["end"] - form.cleaned_data["birthyear"]),
            },
        )
    else:
        return render(request, "age.html", {"form": form})


def order_view(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("{:.2f}".format(((burgers * 4.5) + (fries * 1.5) + drinks)))
    form = OrderForm(request.GET)
    if form.is_valid():
        return render(
            request,
            "order.html",
            {
                "form": form,
                "burgers": form.cleaned_data["burgers"],
                "fries": form.cleaned_data["fries"],
                "drinks": form.cleaned_data["drinks"],
                "total": "{:.2f}".format(
                    (form.cleaned_data["burgers"] * 4.5)
                    + (form.cleaned_data["fries"] * 1.5)
                    + form.cleaned_data["drinks"]
                ),
            },
        )
    else:
        return render(request, "order.html", {"form": form})
