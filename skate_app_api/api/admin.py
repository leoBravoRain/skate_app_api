# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Location, Videos_Location, Place

# Register your models here.

admin.site.register(Location)
admin.site.register(Videos_Location)
admin.site.register(Place)