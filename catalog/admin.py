from django.contrib import admin

# Register your models here.
from catalog.models import Fighter, Record

# admin.site.register(Fighter)
admin.site.register(Record)
@admin.register(Fighter)
class FighterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'nick_name', 'last_name', 'display_record']
