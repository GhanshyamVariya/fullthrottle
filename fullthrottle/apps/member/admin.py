from django.contrib import admin

# Register your models here.
from fullthrottle.apps.member.models import Member, Activity


class ActivityAdmin(admin.TabularInline):
    model = Activity
    readonly_fields = ('id', 'start_time', 'end_time')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('uid', 'name', 'time_zone', 'created_ts')
    readonly_fields = ('uid', 'name', 'time_zone', 'created_ts')
    search_fields = ('uid', )
    inlines = (ActivityAdmin,)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Member, MemberAdmin)
