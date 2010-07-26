from django.conf.urls.defaults import *
import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='events'),
    url(r'^schedule$', views.schedule, name='schedule'),
)
