from django.contrib import admin
from .models import Farmer, Counselor, PredictedDisease
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Counselor)
admin.site.register(PredictedDisease)
