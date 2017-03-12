from django.contrib import admin

from .models import Man

class FollowingInline(admin.TabularInline):
    model = Man.followings.through
    fk_name = 'from_man'


class FollowersInline(admin.TabularInline):
    model = Man.followings.through
    fk_name = 'to_man'

class ManAdmin(admin.ModelAdmin):
	readonly_fields = ['id']
	fields = ('id', 'name',)
	list_display = ['name', 'count_followings', 'count_followers',]
	inlines = (FollowingInline, FollowersInline,)
	

admin.site.register(Man, ManAdmin)