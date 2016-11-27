from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, amigos! You're at the news index.")
