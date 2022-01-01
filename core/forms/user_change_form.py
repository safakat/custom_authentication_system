from django import forms

from core.models.users_model import User

from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email', 'password', 'date_of_birth', 'is_active', 'is_admin')