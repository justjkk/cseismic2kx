from django.conf.urls.defaults import *
import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='events'),
    url(r'^(?P<slug>[-\w]+)/', views.event_details, name='event_details'),
    url(r'^schedule$', views.schedule, name='schedule'),
)
