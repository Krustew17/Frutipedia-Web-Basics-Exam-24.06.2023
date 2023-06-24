from django import forms

from fruitipedia_app.profile_app.models import ProfileModel


class BaseProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="",
                               widget=(forms.PasswordInput(attrs={'placeholder': 'Password'})))

    class Meta:
        model = ProfileModel
        fields = ()


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'email', 'password')


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    image = forms.URLField(label="Image URL", required=False)
    age = forms.IntegerField(label="Age")

    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'image', 'age')
