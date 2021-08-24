from django.urls import path
# from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('<int:id>', views.meeting_detail, name="meeting_detail"),
    path('rooms_list', views.rooms_list, name="rooms_list"),
    path('rooms/<int:id>', views.room_detail, name="room_detail"),
    path('new_meeting', views.new_meeting, name="new_meeting"),
    path('new_room', views.new_room, name="new_room"),
]