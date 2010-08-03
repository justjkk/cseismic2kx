from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import time

from models import Event

def index(request):
    events = Event.objects.all()
    return render_to_response('events/index.html', {'events': events}, context_instance=RequestContext(request), mimetype='text/html')
    
def schedule(request):
    events = Event.objects.all()
    scheduled_events = [(e.caption, e.start_time, e.end_time, e.venue) for e in events]
    scheduled_events += (('Inaugeration Function', time(9), time(10,30), 'KMC Auditorium'),)
    scheduled_events += (('Lunch', time(12), time(13), 'Canteen'),)
    scheduled_events += (('Valedictory & Prize distribution', time(16), None, 'Digital Library'),)
    for i in range(0,len(scheduled_events)):
        if scheduled_events[i][1] is None:
            scheduled_events[i] = scheduled_events[i][:1] + ('-',) + scheduled_events[i][2:]
        if scheduled_events[i][2] is None:
            scheduled_events[i] = scheduled_events[i][:2] + ('-',) + scheduled_events[i][3:]

    scheduled_events.sort(key=lambda x: str(x[1]))
    return render_to_response('events/schedule.html', {'events': scheduled_events}, context_instance=RequestContext(request), mimetype='text/html')
