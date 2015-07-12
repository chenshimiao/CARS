from django.contrib import admin

# Register your models here.
from .models import TutorialItem

class TutorialItemAdmin(admin.ModelAdmin):
    fields=['level','title','distance','price','time','city','gearbox']
    list_display=('level','title','distance','price','time','city','gearbox')
    list_filter=['gearbox']
    search_fields=['title']
    
admin.site.register(TutorialItem,TutorialItemAdmin)
