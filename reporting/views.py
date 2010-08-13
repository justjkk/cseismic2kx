from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
import reporting

def report_list(request):
    reports = reporting.all_reports()
    return render_to_response('reporting/list.html', {'reports': reports}, 
                              context_instance=RequestContext(request))

@staff_member_required
def view_report(request, slug):
    report = reporting.get_report(slug)(request)
    data = {'report': report, 'title':report.verbose_name}
    return render_to_response('reporting/view.html', data, 
                              context_instance=RequestContext(request))
