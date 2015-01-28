from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'searchproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',include('searchapp.urls',namespace="searchapp")),
    (r'^search/', include('haystack.urls')),
    url(r'^create/$', 'searchapp.views.create_note', name='create'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__alohaeditor__/', include('aloha_editor.urls', namespace='aloha_editor')),
)
