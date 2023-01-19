"""
Definition of forms.
"""

from django.forms import ModelForm
from .models import Animal

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class SearchAnimal(forms.Form):
    ani_option = (('Cat', 'Cat'), ('Dog', 'Dog'), ('Any', 'Any'))
    ani_class = (('Young', 'Young'), ('Adult', 'Adult'), ('Senior', 'Senior'), ('Any', 'Any'))
    ani_size = (('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Any', 'Any'))
    ani_activity_level = (('Small', 'Small'), ('Medium', 'Medium'), ('High', 'High'), ('Any', 'Any'))
    yes_no = (('No', 'no'), ('Yes', 'yes'))
    filter_type = forms.ChoiceField(label="Are you looking for a cat or a dog?",
                    choices=ani_option)
    filter_class = forms.ChoiceField(label="What Age of animal are you looking for?",
                    choices=ani_class)
    filter_likes_dog = forms.ChoiceField(label="Do you currentlty have dogs?", choices=yes_no)
    filter_likes_cat = forms.ChoiceField(label="Do you currentlty have cats?", choices=yes_no)
    filter_likes_kids = forms.ChoiceField(label="Do you currentlty have kids?", choices=yes_no)
    filter_size = forms.ChoiceField(label="What animal are you interested in?",
                    choices=ani_size)
    filter_activity_level = forms.ChoiceField(label="What Activity level do you desire in an animal?",
                    choices=ani_activity_level)