from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest


def home(request: HttpRequest):
    if request.method != "GET":
        return HttpResponseBadRequest(b"This method is not allowed!")
    return render(request, "index.html")
