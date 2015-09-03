# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.forms import CharField, PasswordInput, ValidationError

from extuser.models import ExtUser


class ExtUserCreationForm(UserCreationForm):
    password1 = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password Confirmation', widget=PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = ExtUser
        fields = ('email', 'username')

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            ExtUser._default_manager.get(username=username)
        except ExtUser.DoesNotExist:
            return username
        raise ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class ExtUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label='password', help_text='There is no way to see this password.')

    class Meta(UserChangeForm.Meta):
        model = ExtUser
        fields = ('username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')

    def clean_password(self):
        return self.initial['password']
