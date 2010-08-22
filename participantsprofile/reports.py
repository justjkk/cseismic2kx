import reporting
from django.db.models import Sum, Avg, Count
from models import Participant

class ParticipantReport(reporting.Report):
    model = Participant
    verbose_name = 'Participant Report'
    annotate = (                    # Annotation fields (tupples of field, func, title)
        ('id', Count, 'Total'),     # example of custom title for column 
    )
    aggregate = (                   # columns that will be aggregated (syntax the same as for annotate)
        ('id', Count, 'Total'),
    )
    group_by = [                   # list of fields and lookups for group-by options
        'college',
        #'user',
    ]
    list_filter = [                # This are report filter options (similar to django-admin)
        'user__user__is_active',
        'events',
        'college',
    ]
    
    detail_list_display = [        # if detail_list_display is defined user will be able to see how rows was grouped  
        'name', 
        'college',
        'roll_no',
        'phone_no',
        'email_id',
    ]

reporting.register('participant', ParticipantReport) # Do not forget to 'register' your class in reports
