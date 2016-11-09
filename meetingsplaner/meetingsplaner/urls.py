"""meetingsplaner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mpapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.start_page, name="start"),
    url(r'^profile/(?P<uid>\d+)/$', views.display_user, name="profile"),
    url(r'^users/', views.users_list, name="users"),
    url(r'^meetings/', views.meetings_list, name="meetings"),
    url(r'^meeting/(?P<mid>\d+)/$', views.display_meeting, name="meeting"),
    url(r'^newmeeting/', views.create_event, name="newmeeting"),
    url(r'^event_created/', views.members_addition, name="event_created"),

]
# url(r'^meeting/(?P<mid>\d+)/$', views.members_list, name = "members_list"),]
# url(add_event views.add_event)
