from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Event

def index(request):
    events = Event.objects.all()
    return render_to_response('events/index.html', {'events': events}, context_instance=RequestContext(request), mimetype='text/html')
