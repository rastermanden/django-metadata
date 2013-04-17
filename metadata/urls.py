# urls.py
from django.conf.urls import patterns, url
from metadata.views import MetadataList, MetadataDetail
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    url(r'^$', lambda x: HttpResponseRedirect('/list/')), ##http://matthowell.com/blog/2009/12/12/django-url-redirect-shortcut/
    url(r'^list/', MetadataList.as_view(), name='list'),
    url(r'^detail/(?P<slug>[-_\w]+)/$', MetadataDetail.as_view(), name='detail'),

)