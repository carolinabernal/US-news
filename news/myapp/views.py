# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
from os.path import join
from django.conf import settings
import pandas as pd

def newshome(request):
    return render(request, 'newshome.html')

def Trumptab(request):
    return render(request, 'Trumptab.html')

def Hillarytab(request):
    return render(request, 'Hillarytab.html')

def marihuanatab(request):
    return render(request, 'marihuanatab.html')

def Cubatab(request):
    return render(request, 'Cubatab.html')

def picget(request, w):
    import webbrowser
    return HttpResponse(webbrowser.open("https://github.com/carolinabernal/US-news/raw/master/{}.png".format(w)))
