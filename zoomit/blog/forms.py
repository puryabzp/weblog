from django import forms
# from django.contrib.auth import authenticate, get_user_model
# from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CommentForm(forms.Form):
    content = forms.CharField(label=_("  "), widget=forms.Textarea, required=True)


class LikeCommentForm(forms.Form):
    condition = forms.CharField()
    comment = forms.IntegerField()
