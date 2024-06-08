from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','first_name','last_name']

class UpdateUserForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields=['username','email','first_name','last_name']