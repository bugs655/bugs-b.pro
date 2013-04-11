from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>Точное время %s.</body></html>" % now
    return render(request, 'index.html')
