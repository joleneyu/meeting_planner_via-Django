from django.db.models.aggregates import Count
# from meeting_planner.meetings.models import Meeting
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html", 
                  {"message": "This data was sent from the view to the template.",
                  "num_meetings": Meeting.objects.count(),
                  "all_meetings": Meeting.objects.all(),
                  }
                  )

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi Jolene here! I came to Australia almost 4 years ago!")
# Create your views here.
