from django.contrib import admin
from .models import rideshare
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('startl', 'lastl','date','stavl','dlphoto')
    
admin.site.register(rideshare, SettingAdmin)
