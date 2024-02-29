from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        # print(type(self.cleaned_data))
        # print(self.cleaned_data)
        # cd = self.changed_data
        # print(type(cd))
        # print(cd)
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Password don't match. ")
        return self.cleaned_data["password2"]
