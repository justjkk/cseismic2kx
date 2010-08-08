from django import forms
from registration.forms import RegistrationForm
from models import UserProfile
from registration.models import RegistrationProfile
from models import College
from events.models import Event
from captcha.fields import CaptchaField

def get_colleges_list():
    colleges_list = ()
    for c in College.objects.order_by('name'):
        colleges_list += ((c.id, c.name),)
    colleges_list += ((-1,'Add my College'),)
    return colleges_list

def get_events_list():
    events_list = ()
    for e in Event.objects.all():
        events_list += ((e.id, str(e)),)
    return events_list

class UserRegistrationForm(RegistrationForm):
    fullname = forms.CharField()
    phone_no = forms.IntegerField()
    college = forms.ChoiceField(choices=())
    add_your_college = forms.CharField(required=False, help_text='Enter your college name if not chosen above')
    rollno = forms.CharField()
    events = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple, required=False)
    captcha = CaptchaField(help_text='Type the characters you see on the left in the above textbox')
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['college'].choices = get_colleges_list()
        self.fields['events'].choices = get_events_list()
        
class ParticipantEventsForm(forms.Form):
    events = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple, required=False)
    
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['events'].choices = get_events_list()
