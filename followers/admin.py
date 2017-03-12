from django.contrib import admin

from .models import Man

class ManAdmin(admin.ModelAdmin):
	list_display = ['name', 'count_followings', 'count_followers',]
	

admin.site.register(Man, ManAdmin)