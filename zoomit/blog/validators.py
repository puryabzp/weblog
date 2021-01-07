from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


def validate_username(username):
    try:
        User.objects.get(username=username)
        raise ValidationError(_('user is already exist'), code='invalid')
    except User.DoesNotExist:
        pass


def validate_password(password):
    if len(password) < 6:
        raise ValidationError(_('password is lower than 8'), code='invalid')
