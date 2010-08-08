from django.template import RequestContext
from django.shortcuts import render_to_response
from home.models import NewsItem
from events.models import Event

def index(request):
    news_items = NewsItem.objects.order_by('-date')[:5]
    return render_to_response('index.html', {'news_items' : news_items}, context_instance=RequestContext(request), mimetype='text/html')

def gallery(request):
    return render_to_response('gallery.html', context_instance=RequestContext(request), mimetype='text/html')

def sitemap(request):
    e = Event.objects.all()
    return render_to_response('sitemap.html', {'events': e}, context_instance=RequestContext(request), mimetype='text/html')
