from django.contrib import admin
from .models import  Note
# Register your models here.

# class NOTEManager(admin.ModelAdmin):
#     list_display = ['user', 'title', 'content', 'classify', 'create_time', 'update_time']
#     list_display_links = ['title']
#     list_filter = ['user', 'classify']
#     search_fields = ['title']
#
# admin.site.register(Note, NOTEManager)