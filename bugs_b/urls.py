from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bugs_b.views import index
from django.conf import settings
#from django.conf.urls.defaults import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search_form/$',views.search_form),
    #url(r'^search/$',views.search),
    url(r'^$', index),
    #url(r'^css/(?P<path>.*)$','django.contrib.staticfiles',{'document_root': STATIC_ROOT}),
)
urlpatterns += patterns('django.contrib.staticfiles.views', url(r'static/(?P<patch>.*)$','serve'))
