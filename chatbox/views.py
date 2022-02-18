from django.shortcuts import render

from django.http import HttpResponse
def chathome(request):
    return HttpResponse("This is chat homepage")

def chatabout(request):
    return HttpResponse("This is chat aboutpage")

def chatcontact(request):
    return HttpResponse("This is chat contactpage")

