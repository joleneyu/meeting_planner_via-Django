from django.shortcuts import render, get_object_or_404
from meetings.models import Meeting, Room

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
# Create your views here.
