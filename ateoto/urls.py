from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='splash.html')),
    url(r'^admin/', include(admin.site.urls)),
)
