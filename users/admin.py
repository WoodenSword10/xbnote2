from django.contrib import admin
from .models import User_info
# Register your models here.
class User_infoManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'sex', 'email', 'info']
    list_display_links = ['username']
    list_filter = ['sex']
    search_fields = ['username']

admin.site.register(User_info, User_infoManager)