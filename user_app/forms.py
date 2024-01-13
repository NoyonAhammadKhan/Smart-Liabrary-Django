
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, UserDepartment
from .constants import DEPARTMENT_TYPE, FACULTY_TYPE


class UserSignupForm(UserCreationForm):
    department = forms.ChoiceField(choices=DEPARTMENT_TYPE)
    faculty = forms.ChoiceField(choices=FACULTY_TYPE)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'department', 'faculty',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        signup_user = super().save(commit=False)
        if commit == True:
            signup_user.save()
            department = self.cleaned_data.get('department')
            faculty = self.cleaned_data.get('faculty')
            UserAccount.objects.create(
                user=signup_user,
                account_no=1000+signup_user.id,
            )
            UserDepartment.objects.create(
                user=signup_user,
                department=department,
                faculty=faculty
            )

        return signup_user
