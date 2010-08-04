from django import forms
from registration.forms import RegistrationForm
from models import UserProfile
from registration.models import RegistrationProfile
from models import College

def get_colleges_list():
    colleges_list = ()
    for c in College.objects.order_by('name'):
        colleges_list += ((c.id, c.name),)
    colleges_list += ((-1,'Add my College'),)
    return colleges_list

class UserRegistrationForm(RegistrationForm):
    fullname = forms.CharField()
    phone_no = forms.IntegerField()
    college = forms.ChoiceField(choices=())
    add_your_college = forms.CharField(required=False, help_text='Enter your college name if not chosen above')
    rollno = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['college'].choices = get_colleges_list()
