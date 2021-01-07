from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm

from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff']
    change_password_form = AdminPasswordChangeForm
    ordering = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (_('authentication data'), {
            "fields": (
                'email',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('full_name', 'avatar')
        }),
        (_('Permissions'), {
            "fields": ('is_staff', 'is_active', 'is_superuser','groups','user_permissions')
        }),
        (_('Important dates'), {
            "fields": ('last_login',)
        }),
    )


# Register your models here.
admin.site.register(User, UserAdmin)



















































# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import AdminPasswordChangeForm
# from django.utils.translation import ugettext_lazy as _
#
# from .models import User
#
#
# # Register your models here.
#
# class UserAdmin(BaseUserAdmin):
#     list_display = ['username', 'email']
#     change_password_form = AdminPasswordChangeForm
#     add_fieldsets = ((None, {
#         'classes': ('wide',),
#         'fields': ('username', 'email', 'password1', 'password2')}))
#     fieldsets = (
#         (None, {
#             'fields': ('username', 'email', 'password')
#         }),
#         (_('Personal info'), {
#             'fields': ('first_name', 'last_name'),
#         }),
#         (_('Permissions'), {
#             'fields': ('is_staff', 'is_active', 'is_superuser'),
#         }),
#         (_('Important Dates'), {
#             'fields': ('last_login', 'date_joined'),
#         }),
#     )
#
#
# admin.site.register(User, UserAdmin)
