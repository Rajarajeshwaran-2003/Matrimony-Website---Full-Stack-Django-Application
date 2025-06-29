# this is admin.py

from django.contrib import admin
from .models import Candidate, Testimony

admin.site.register(Candidate)
admin.site.register(Testimony)
