from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^places/$', places),
    url(r'^$', main_page),
    url(r'^choices/$', choices),
    url(r'^result/$', result), 
)

'''
url(r'^admin/', include(admin.site.urls)),
url(r'^hello/$', hello),
url(r'^time/$', current_datetime),
url(r'^another-time-page/$', current_datetime),
url(r'^time/plus/(\d{1,2})/$', hours_ahead),
url(r'^welcome/$', current_url_view_good),
url(r'^search-form/$', search_form),
url(r'^search/$', search),
'''