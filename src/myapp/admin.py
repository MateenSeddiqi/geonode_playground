from django.contrib import admin
from .models import OchaDashboard
from django import forms
from myapp.models import OchaDashboard,ProfileProxy
from import_export.admin import ExportActionMixin
from django.utils.translation import gettext_lazy as _



class ProfileProxyAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ("id", "username", "organization", "email", "first_name", "last_name", "is_staff", "is_active","last_login","date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups",'date_joined')
    search_fields = ("username", "organization", "profile", "first_name", "last_name", "email")
    # readonly_fields = ("groups", )
    ordering = ("date_joined",)
    
    # date_hierarchy = 'date_joined'
    
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    
    # This will help you to disable change functionality
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(ProfileProxy,ProfileProxyAdmin)


class OchaDashboardAdminForm(forms.ModelForm):
    class Meta:
        model = OchaDashboard
        exclude = ('slug',)
        
class OchaDashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','updated','created')
    # prepopulated_fields = {"slug": ("name",)}
    form = OchaDashboardAdminForm

admin.site.register(OchaDashboard,OchaDashboardAdmin)

