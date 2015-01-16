from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'searchproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',include('searchapp.urls')),
    (r'^search/', include('haystack.urls')),
    url(r'^create/$', 'searchapp.views.create_note', name='create'),
    url(r'^admin/', include(admin.site.urls)),
)
