from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from mpapp import models
from models import forms
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from datetime import timedelta

def start_page(request):
    name_list = models.Profile.objects.all()
    return render(request, 'index.html', {'name_list': name_list})


def display_user(request, uid):
    profile = models.Profile.objects.get(pk=uid)
    return render(request, 'profile.html', {'profile': profile})

def display_meeting(request, mid):
    meeting = models.Meetings.objects.get(id=mid)
    members = meeting.Members.all()
    return render(request, 'meeting.html', {'meeting': meeting, 'members': members})

def users_list(request):
    name_list = models.Profile.objects.all()
    return render(request, 'users.html', {'name_list': name_list})

def meetings_list(request):
    meetings_list = models.Meetings.objects.all()
    return render(request, 'meetings.html', {'meetings_list': meetings_list})

def members_list(request, mid):
    members_list = models.UsersMeetings.objects.get(id=mid)
    return render(request, 'meetings.html', {'members_list': members_list})

newevent = 0

def create_event(request):
    form_list = ['event_name', 'start_time', 'duration']
    if request.method == 'POST':
        data = []
        for line in form_list:
            data.append(request.POST[line].split('/n'))

        new_event = models.Meetings()
        new_event.Name = data[0][0]
        new_event.Start = data[1][0]
        duration = datetime.strptime(data[2][0], '%H')
        duration_delta = timedelta(microseconds=1000000 * 3600 * duration.hour)
        new_event.Duration = duration_delta

        new_event.Finish = "0:00:00"

        startminuteslist = []
        for elem in str(new_event.Start).split(':'):
            startminuteslist.append(elem)

        startminutes = 0
        startminutes = int(startminuteslist[0]) * 60 + int(startminuteslist[1])
        finishminutes = startminutes + int(str(new_event.Duration).split(':')[0]) * 60 + int(str(new_event.Duration).split(':')[1])
        finishdate = ""
        #if finishminutes/60 => 24:

        finishdate += str(finishminutes/60)+ ":" + str(finishminutes//60 + 1)+ ":" + str(finishminutes//3600)

        #new_event.Finish = finishdate
        print startminuteslist
        print startminutes
        print finishminutes
        print finishdate

        new_event.save()
        name_list = models.Profile.objects.all()
        global newevent
        newevent = new_event.id
        return render(request, 'newmeeting.html', {'event': new_event, 'name_list': name_list})
    return render(request, 'newmeeting.html', {'event': new_event, 'name_list': name_list})

def members_addition(request):
    current_event = models.Meetings.objects.get(id=newevent)
    data = []
    for param in request.GET:
        data.append(param)
    current_event.Members = data
    members = current_event.Members.all()
    startseconds = list(str(current_event.Start).split(':'))
    startseconds = int(startseconds[0])*60+int(startseconds[1])
    durationseconds = list(str(current_event.Duration).split(':'))
    durationseconds = int(durationseconds[0])*60+int(durationseconds[1])
    users_start = []
    for member in members:
        users_start.append(list(str(member.WorkingTime).split(':')))

    users_finish = []
    for member in members:
        users_finish.append(list(str(member.FinishTime).split(':')))

    users_finish_ints = []
    for elem in users_finish:
        users_finish_ints.append(int(elem[0])*60+int(elem[1]))

    users_start_ints = []
    for elem in users_start:
        users_start_ints.append(int(elem[0])*60+int(elem[1]))

    message = "empty"

    print "startseconds = " + str(startseconds)
    print "durationseconds = " + str(durationseconds)
    print "users_start = " + str(users_start)
    print "users_start_ints = " + str(users_start_ints)

    for item in users_start_ints:
        if item > startseconds or item+8*60 < startseconds+durationseconds:
            current_event.delete()
            message = "Event creation is impossile"
            return render(request, 'event_created.html', {'message': message})
        else:
            return render(request, 'event_created.html', {'meeting': current_event, 'members': members, 'message': message})





