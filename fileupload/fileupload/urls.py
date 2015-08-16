from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fileupload.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('rat.urls')),
    url(r'^$', 'fileupload.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
