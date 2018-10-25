from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html')

def routefinder(request):
    return render_to_response('route.html')
    #shows the route to the user
