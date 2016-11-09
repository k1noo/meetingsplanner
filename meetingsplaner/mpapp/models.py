from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django import forms


class Profile(models.Model):
    ProfileUser = models.ForeignKey(User)
    WorkingTime = models.TimeField()
    FinishTime = models.TimeField()
    BusyTime = models.CharField(max_length=100)

    def __str__(self):
        return str(self.ProfileUser.first_name) + ' ' + str(self.ProfileUser.last_name)


class Meetings(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.DurationField()
    Start = models.TimeField()
    Finish = models.TimeField()
    Members = models.ManyToManyField(Profile)

    def __str__(self):
        return str(self.Name)


class UsersMeetings(models.Model):
    MeetingLink = models.ForeignKey(Meetings)
    Members = models.ForeignKey(Profile)

    def __str__(self):
        return str(self.MeetingLink.Name) + ': ' + str(self.Members)


class NewMeeting(forms.Form):
    Name = forms.CharField(max_length=100)
    Duration = forms.DurationField()
    Start = forms.TimeField()
    Members = forms.ModelMultipleChoiceField(queryset=Meetings.objects.all())

# Create your models here.
# Inherite from django.contrib.auth.models.User
