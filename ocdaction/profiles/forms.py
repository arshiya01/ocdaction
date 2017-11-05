from django import forms

from profiles.models import OCDActionUser
from registration.forms import RegistrationForm
import datetime


class OCDActionUserRegistrationForm(RegistrationForm):
    """custom registration form
    """
    yes_no_choices = (
        (1, 'Yes'),
        (0, 'No'),
    )

    have_ocd = forms.ChoiceField(
        choices=yes_no_choices,
        label='Do you have an OCD diagnosis?'
    )

    now = datetime.datetime.now()
    current_year = now.year
    users_average_age = 20
    date_birth = forms.DateField(widget=forms.SelectDateWidget(
        years=range(current_year - users_average_age, current_year)),
        label='Date of birth'
    )
    terms = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-checkbox'}),
        error_messages={'required': 'You must accept the terms and conditions'},
        label="I agree to the terms and conditions"
    )

    class Meta:
        """a challenge is a user created challenge that can be completed
        by a user to track anxiety
        """
        model = OCDActionUser
        fields = ('email', 'password1', 'password2', 'username', 'date_birth')
