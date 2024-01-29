from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'avatar', 'phone', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class PasswordResetForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
