from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^agenda$', "cms_users_put.views.all"),
    url(r'^agenda/(.*)$', "cms_users_put.views.number"),
    url(r'^(.*)$', "cms_users_put.views.notfound"),
)
