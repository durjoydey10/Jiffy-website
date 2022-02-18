from django.shortcuts import render

from django.http import HttpResponse
def storyhome(request):
    return HttpResponse("This is story homepage")

def storyabout(request):
    return HttpResponse("This is story aboutpage")

def storycontact(request):
    return HttpResponse("This is story contact page")
