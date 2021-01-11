from django.contrib import admin

# Register your models here.
from . models import about
from . models import slider
from . models import client

# register into database
admin.site.register(about)
admin.site.register(slider)
admin.site.register(client)