from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

'''
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q'].encode()
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''

def places(request):
    return render(request, 'places.html')

def main_page(request):
    return render(request, 'main.html')

def choices(request):
    return render(request, 'choices.html')

def result(request):
    return render(request, 'result.html')

def votes(request):  
    people = raw_input("Num_ppl: ")
    html = "<html><body> Y'all had %s  <p></body></html>" % (people)
    choices = raw_input("Num_restaurants: ")
    html += "<html><body> Y'all had %s choices <p></body></html>"%(choices)
    try:
        people = int(people)
        choices = int(choices)
    except ValueError:
            raise Http404()    
        
    score = [[0 for col in range(choices)] for row in range(people)]
    tally = [0] * choices
    names = [""] * choices
    
    for i in range(choices):
        names[i] = raw_input("Name of restaurant %s: " % (i + 1))
    winner = 0
    
    for i in range(people):
        for j in range(choices):
            rank = raw_input("Person %s : How do you rank %s (1-10): " % (i + 1,names[j]))
            try:
                rank = int(rank)
            except ValueError:
                raise Http404() 
            score[i][j] += rank
            
    for j in range(choices):
        score_sum = 0
        for i in range(people):
            score_sum += score[i][j]
        tally[j] = score_sum
        if (tally[j] >= tally[winner]): winner = j
        
        
            
    html += "<html><body><p>Winner: %s.</body></html>" % (names[winner])   
    return HttpResponse(html)
