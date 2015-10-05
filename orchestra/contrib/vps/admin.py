from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from orchestra.admin import ExtendedModelAdmin, ChangePasswordAdminMixin
from orchestra.contrib.accounts.actions import list_accounts
from orchestra.contrib.accounts.admin import AccountAdminMixin
from orchestra.forms import UserCreationForm, NonStoredUserChangeForm

from .models import VPS


class VPSAdmin(ChangePasswordAdminMixin, AccountAdminMixin, ExtendedModelAdmin):
    list_display = ('hostname', 'type', 'template', 'account_link')
    list_filter = ('type', 'template')
    form = NonStoredUserChangeForm
    add_form = UserCreationForm
    readonly_fields = ('account_link',)
    change_readonly_fields = ('account', 'hostname', 'type', 'template')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_link', 'hostname', 'type', 'template')
        }),
        (_("Login"), {
            'classes': ('wide',),
            'fields': ('password',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account', 'hostname', 'type', 'template')
        }),
        (_("Login"), {
            'classes': ('wide',),
            'fields': ('password1', 'password2',)
        }),
    )
    actions = (list_accounts,)
    
    def get_change_password_username(self, obj):
        return 'root@%s' % obj.hostname


admin.site.register(VPS, VPSAdmin)
