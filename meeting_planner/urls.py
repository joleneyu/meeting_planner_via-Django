"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from meeting_planner.website.views import welcome
# from meeting_planner.meetings.views import rooms_list
from django.contrib import admin
from django.urls import path, include
from website.views import welcome, date, about
# from meetings.views import meeting_detail, room_detail, rooms_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('date', date),
    path('about', about),
    path('meetings/', include('meetings.urls')),
    # path('meeting_detail/<int:id>', meeting_detail, name="meeting_detail"),
    # path('room_detail/<int:id>', room_detail, name="room_detail"),
    # path('rooms_list', rooms_list, name="rooms_list"),
]
