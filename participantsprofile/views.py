from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import ParticipantEventsForm

@login_required
def participant_events(request):
    if request.method == 'POST':
        try:
            participant = request.user.get_profile().participant_set.all()[0]
        except Exception:
            return HttpResponse('This page is not for you!<br><a href="/">Take me back Home</a>')
        form = ParticipantEventsForm(request.POST)
        participant.events = form.data.getlist('events')
        for e in form.data.getlist('events'):
            if e not in [e.id for e in participant.events.all()]:
                participant.events.add(e)
        return HttpResponseRedirect('/')
    else:
        try:
            participant = request.user.get_profile().participant_set.all()[0]
        except Exception:
            return HttpResponse('This page is not for you!<br><a href="/">Take me back Home</a>')
        events = [ e.id for e in participant.events.all()]
        form = ParticipantEventsForm(data = {'events':events})
    return render_to_response('participantsprofile/participant_events.html', {'form':form}, context_instance=RequestContext(request), mimetype='text/html')
