from django.shortcuts import render_to_response
from django.template import RequestContext

def contact_us(request):
    return render_to_response('host/contact_us.html', context_instance=RequestContext(request), mimetype='text/html')
