from django.contrib import admin

# Register your models here.
from .models import Magazin,Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','gul')
    fields = ['name', 'gul']

admin.site.register(Client, ClientAdmin)
admin.site.register(Magazin)