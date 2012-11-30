from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from mezzanine.core.views import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^testapp/', include('testapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='main.html'), name='home'),
    url(r'qui/', TemplateView.as_view(template_name='who.html'), name='index'),
    ("^godmode/", include(admin.site.urls)),
#    url("^$", direct_to_template, {"template": "main.html"}, name="home"),
    ("^", include("mezzanine.urls")),
#    ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))
)

handler500 = "mezzanine.core.views.server_error"
