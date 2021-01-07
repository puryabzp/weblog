from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import User


class SignInForm(AuthenticationForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(email=username)
        except User.DoesNotExist:
            raise ValidationError(_('همچین ایمیلی موجود نیست!'))
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=username)
            if not check_password(password, user.password):
                raise ValidationError(_('پسوورد غلطه!!!'))

        except User.DoesNotExist:
            pass

        return password


# class LoginForm(forms.Form):
#     username = forms.EmailField(label=_('نام کاربری'), required=True, help_text=_('در نظر داشته باشید نام کاربری شما '
#                                                                                   'همان ایمیل شما میباشد'))
#     password = forms.CharField(label=_('رمز عبور'), widget=forms.PasswordInput, required=True)
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         try:
#             User.objects.get(email=username)
#         except User.DoesNotExist:
#             raise ValidationError(_('همچین ایمیلی موجود نیست!'))
#         return username
#
#     def clean_password(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         try:
#             user = User.objects.get(email=username)
#             if not check_password(password, user.password):
#                 raise ValidationError(_('پسوورد غلطه!!!'))
#
#         except User.DoesNotExist:
#             pass
#
#         return password


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label=_('تایید پسوورد'), required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'password2')
        widgets = {
            'email': forms.EmailInput, 'full_name': forms.TextInput, 'password': forms.PasswordInput
        }
        labels = {'email': _('ایمیل کاربری'), 'password': _('رمز عبور'),
                  'full_name': _('نام و نام خانوادگی')}

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise ValidationError(_('رمز عبور و تایید رمز عبور مغایر هستند!'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError(_(f'کاربری با ایمیل   {email}  در حاضر عضو میباشد ایمیل دیگری وارد نمایید'))
        except User.DoesNotExist:
            pass
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        try:
            User.objects.get(full_name=full_name)
            raise ValidationError(_(f'کاربری با نام  {full_name}  موجود است'))
        except User.DoesNotExist:
            pass
        return full_name
