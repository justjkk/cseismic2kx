from django.conf.urls.defaults import *
import views
urlpatterns = patterns('',
    url(r'^$', views.show_route, name='bus_routes'),
    url(r'^(?P<id>\d+)/', views.show_route, name='show_route'),
)
