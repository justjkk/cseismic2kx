from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

from home.feeds import LatestNewsFeed

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cseismic2kx/', include('cseismic2kx.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^$', 'home.views.index'),
    url(r'^account/activate/(?P<activation_key>\w+)/$', 'registration.views.activate', { 'backend': 'registration.backends.default.DefaultBackend' }, name='registration_activate'),
    url(r'^account/activate/complete/$', direct_to_template, { 'template': 'registration/activation_complete.html' }, name='registration_activation_complete'),
    url(r'^account/signup/$', 'registration.views.register', {'backend':'registration.backends.default.DefaultBackend' }, name='registration_register'),
    (r'^account/', include('django_authopenid.urls')),
    (r'^feed/rss/', LatestNewsFeed()),
)
