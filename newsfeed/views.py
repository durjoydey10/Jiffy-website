from django.shortcuts import render

from  django.http import HttpResponse
def homepage(request):
    return HttpResponse ("This is homepage")

def aboutpage(request):
    return HttpResponse("This is aboutpage")

def contactpage(request):
    return HttpResponse("This is contact page")
