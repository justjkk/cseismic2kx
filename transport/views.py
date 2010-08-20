from django.shortcuts import get_object_or_404
from models import CollegeBus, Stop
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse

def show_route(request, id=1):
    buses = CollegeBus.objects.all()
    b = get_object_or_404(CollegeBus,pk=id)
    stops = b.stops.order_by('stop_timings__sequence')
    all_stops = Stop.objects.exclude(pk__in=[s.id for s in stops])
    return direct_to_template   (
            request, 
            'transport/show_route.html', 
            {
                'buses':buses,
                'all_stops':all_stops,
                'bus':b,
                'stops':stops,
            })
def index(request):
   return HttpResponse('Yet to be implemented')
