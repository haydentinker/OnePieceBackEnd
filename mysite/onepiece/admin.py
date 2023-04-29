from django.contrib import admin

# Register your models here.
from .models import Character, Affiliations,Occupations

admin.site.register(Affiliations)
admin.site.register(Occupations)
admin.site.register(Character)