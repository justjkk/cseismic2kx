from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.views.generic.simple import redirect_to

import participantsprofile.regbackend
from home.feeds import LatestNewsFeed
from participantsprofile.forms import UserRegistrationForm

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
    url(r'^account/signup/$', 'registration.views.register', {'backend':'registration.backends.default.DefaultBackend', 'form_class':UserRegistrationForm }, name='registration_register'),
    url(r'^account/profile/event/$', 'participantsprofile.views.participant_events', name='participant_events'),
    url(r'^register/closed/$', direct_to_template, { 'template': 'registration/registration_closed.html' }, name='registration_disallowed'),

    (r'^account/', include('django_authopenid.urls')),
    (r'^events/', include('events.urls')),
    url(r'^contact$', 'host.views.contact_us', name='contact_us'),
    url(r'^gallery$', 'home.views.gallery', name='gallery'),    
    (r'^feed/rss/', LatestNewsFeed()),
    url(r'^sitemap$', 'home.views.sitemap', name='sitemap'),
    url(r'^robots\.txt$', lambda req: redirect_to(req,'/static/robots.txt')),
    (r'^favicon.ico$', lambda req: redirect_to(req,'/static/images/favicon.ico')),
    url(r'^sitemap\.xml$', lambda req: redirect_to(req,'/static/sitemap.xml'))
)
