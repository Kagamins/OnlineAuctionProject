from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','Date_Of_Birth')
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject','date_time_sent')
admin.site.register(User,UserAdmin)
admin.site.register(message,MessageAdmin)

# Register your models here.
