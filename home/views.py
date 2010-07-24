from django.template import RequestContext
from django.shortcuts import render_to_response
from home.models import NewsItem

def index(request):
    news_items = NewsItem.objects.order_by('-date')[:5]
    return render_to_response('index.html', {'news_items' : news_items}, context_instance=RequestContext(request), mimetype='text/html')


