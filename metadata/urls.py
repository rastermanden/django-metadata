# urls.py
from django.conf.urls import patterns, url
from metadata.views import MetadataList, MetadataDetail

urlpatterns = patterns('',
    url(r'^', MetadataList.as_view(), name='list'),
    url(r'^detail/(?P<slug>[-_\w]+)/$', MetadataDetail.as_view(), name='detail'),

)