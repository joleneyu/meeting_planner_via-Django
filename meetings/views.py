from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting, Room
from django.forms import modelform_factory

def meeting_detail(request, id):
    # single_meeting = Meeting.objects.get(pk=id)
    single_meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/meeting_detail.html", 
                  {"meeting": single_meeting,
                  }
                  )

def room_detail(request, id):
    single_room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room_detail.html",
                  {"room": single_room,
                  }
                  )

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", 
                  {"num_rooms": Room.objects.count(),
                  "all_rooms": Room.objects.all(),
                  }
                  )

MeetingForm = modelform_factory(Meeting, exclude=[])

def new_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
        # form has been submitted, process data

    else:    
         form = MeetingForm()
    return render(request, "meetings/new_meeting.html",
                  {"form": form},
                 )

RoomForm = modelform_factory(Room, exclude=[])

def new_room(request):
    if request.method == "POST":
        room_form = RoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
            return redirect("rooms_list")
    else:
        room_form = RoomForm()
    return render(request, "meetings/new_room.html",
                  {"room_form": room_form},
                 )    

# Create your views here.
