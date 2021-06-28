from django.contrib import admin
from .models import Gene, Disease, Variant

admin.site.register(Gene)
admin.site.register(Disease)
admin.site.register(Variant)