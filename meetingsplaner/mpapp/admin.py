from django.contrib import admin
from mpapp import models

admin.site.register([models.Profile,models.Meetings,models.UsersMeetings])

# Register your models here.
