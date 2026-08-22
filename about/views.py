from django.shortcuts import render
from django.http import HttpResponse


def about (requests):
    return HttpResponse("Welcome to about us")
    #return render(requests, "checkins/home.html")
