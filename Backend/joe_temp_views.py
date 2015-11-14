from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def search_form(request):
    return render(request, 'search_form.html')

def hours_ahead(request, offset):
   
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    if(offset == 1):
        html = "<html><body>In %s hour, it will be %s.</body></html>" % (offset, dt)
    else:
        html = "<html><body>In %s hours, it will be %s.</body></html>" % (offset, dt)
    
    return HttpResponse(html)
def votes(request):  
    people = raw_input("How many y'all got: ")
    html = "<html><body> Y'all had %s  <p></body></html>"%(people)
    choices = raw_input("How many places you finna hit up? ")
    html += "<html><body> Y'all had %s choices <p></body></html>"%(choices)
    try:
        people = int(people)  
        choices = int(choices)
    except ValueError:
            raise Http404()    
    score = [0][0] * choices
    for i in range(people):
        for j in range(choices):
            rank = raw_input("Person %s : How do you rank choice %s (1-10): " % (i + 1,j + 1))
            try:
                rank = int(rank)
            except ValueError:
                raise Http404() 
            score[i][j] += rank
    for j in range(choices):
        tally = 0
        for i in range(people):
            tally += score[i][j]
            
        html += "<html><body> <p> The score for choice %s was %s.</body></html>" % (j + 1, score[i][i])   
    return HttpResponse(html)