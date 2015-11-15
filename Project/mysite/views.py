from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime
import random

def main_page(request):
    for key in request.session.keys():
        del request.session[key]
    return render(request, 'main.html')

def places(request):
    try:
        num_people = int(request.GET['num_people'].encode())
        num_places = int(request.GET['num_places'].encode())
    except ValueError:
        raise Http404()
    request.session['num_people'] = num_people
    request.session['num_places'] = num_places
    request.session['person_count'] = 0
    return render(request, 'places.html', {"num_places" : "1" * num_places})

def choices(request):
    request.session['person_count'] += 1
    
    num_people = request.session['num_people']
    num_places = request.session['num_places']    
    
    person_count = request.session['person_count']
    
    #person_score = [0 for x in range(num_places)]
    if (person_count == 1):
        
        request.session['place_names'] = []
        request.session['score'] = [[0 for col in range(num_places)] for row in range(num_people)]
        num_places = request.session['num_places']
        for i in range(num_places):
            request.session['place_names'].append(request.GET["place" + str(i+1)].encode())
    if (person_count > 1):        
        for j in range(num_places):
            try:
                request.session['score'][person_count-2][j] = int(request.GET["rank_" + str(j+1)].encode())
            except ValueError:
                raise Http404()
        
    
    return render(request, 'choices.html', {"num_places" : "1" * request.session['num_places'], "person_num" : person_count, "place_names" : request.session['place_names'], "max_person_num" : request.session['num_people']})

def result(request):
    num_people = request.session['num_people']
    num_places = request.session['num_places']  
    score = request.session['score']
    winner_arr = [0]
    tally = [0 for x in range(num_places)]
    
    for j in range(num_places):
        try:
            request.session['score'][num_people-2][j] = int(request.GET["rank_" + str(j+1)].encode())
        except ValueError:
            raise Http404()
        
    for j in range(num_places):
        score_sum = 0
        for i in range(num_people):
            score_sum += score[i][j]
        tally[j] = score_sum
        if (tally[j] < tally[winner_arr[0]]):
            winner_arr = []
            winner_arr.append(j)
        if (tally[j] == tally[winner_arr[0]]):
            winner_arr.append(j)
    
    r = random.randint(1, len(winner_arr))
    

    return render(request, 'result.html', {"winner" : request.session['place_names'][winner_arr[r-1]]})