from django.conf.urls.defaults import *
import views
urlpatterns = patterns('',
    url(r'^$', views.show_route, name='bus_routes'),
    url(r'^(?P<id>\d+)$', views.show_route, name='show_route'),
    url(r'^text-only/', views.show_route_textonly, name='bus_routes_textonly'),
    url(r'^text-only/(?P<id>\d+)$', views.show_route_textonly, name='show_route_textonly')
)
