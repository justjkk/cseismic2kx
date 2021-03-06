from forms import UserRegistrationForm
from models import UserProfile, Participant, College

def user_created(sender, user, request, **kwargs):
    form = UserRegistrationForm(request.POST)
    user_profile = UserProfile(user=user, user_type='P')
    user_profile.save()
    participant = Participant(user=user_profile)
    participant.name = form.data["fullname"]
    user.firstname = participant.name
    participant.email_id = user.email
    participant.phone_no = form.data["phone_no"]
    if int(form.data["college"]) == -1:
        if form.data["add_your_college"] is not None:
            new_college = College(name=form.data["add_your_college"])
            new_college.save()
            participant.college = new_college
        else:
            raise Exception("No College name specified")
    else:
        participant.college = College.objects.get(pk=form.data["college"])
    participant.roll_no = form.data['rollno']
    participant.save()
    for e in form.data.getlist('events'):
        participant.events.add(e)

def user_verification_updated(sender, user, request, **kwargs):
    participant = Participant.objects.filter(user__user=user)
    if participant is not None and len(participant) == 1:
       participant = participant[0]
       participant.email_verified = 'Yes'
       participant.save()

from registration.signals import user_registered, user_activated
user_registered.connect(user_created)
user_activated.connect(user_verification_updated)
