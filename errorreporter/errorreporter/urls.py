from django.conf.urls import url

from errorreporter import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^login', views.login_page, name='login'),
    url(r'^auth/login', views.perform_login, name='login'),
    url(r'^auth/logout', views.perform_logout, name='logout'),
    url(r'^overview_crashreport_daily$', views.overview_crashreport_daily, name='overview_daily'),
    url(r'^overview_crashreport_version$', views.overview_crashreport_version, name='overview_version'),
    url(r'^crashreport_daily/(?P<date>\d{4}-\d{2}-\d{2})$', views.crashreport_daily, name='crashreport_daily'),
    url(r'^crashreport_version/(?P<version>.+)$', views.crashreport_version, name='crashreport_version'),
    url(r'^stacktrace_graphs/(?P<stack_id>.+)$', views.stacktrace_graphs, name='stacktrace_graphs'),
    url(r'^stacktrace/(?P<stack_id>.+)$', views.stacktrace, name='stacktrace'),
    url(r'^report$', views.report, name='report'),
]
