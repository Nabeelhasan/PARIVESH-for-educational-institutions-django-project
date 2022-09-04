from django import forms
from .models import Proposal

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

LOCATION_CHOICES = [
    ('GIDC Vatva', 'GIDC Vatva'),
    ('Pirana Landfill Site', 'Pirana Landfill Site'),
    ('Laal Darwaza Market', 'Laal Darwaza Market'),
    ('Chhatral Industrial Zone', 'Chhatral Industrial Zone'),
    ('Chandola Industrial Zone', 'Chandola Industrial Zone'),
]

class ProposalForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    locations = forms.MultipleChoiceField(label='Preferred Locations', choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Proposal
        fields = ['name', 'enrollment_no', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'locations', 'proposer_img', 'attachment']
        labels = {'name':'Full Name', 'enrollment_no': 'Enrollment No', 'dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No', 'email':'Email Id', 'proposer_img':'Proposer Image', 'attatchment':'Document'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your full name...'}),
            'enrollment_no':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'180390XXXXXX'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker', 'placeholder':'MM/DD/YYYY'}),
            'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your locality...'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your city...'}),
            'pin':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'XXXXXX'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'XXXXXXXXXX'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@mail.com'}),
        }