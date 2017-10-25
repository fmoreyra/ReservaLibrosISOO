from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from login import views as login_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', login_views.signup, name='signup'),
    url(r'^ajax/validate_username/$', login_views.validate_username, name='validate_username'),
    url(r'^ajax/validate_legajo/$', login_views.validate_legajo, name='validate_legajo'),
    url(r'^ajax/validate_documento/$', login_views.validate_documento, name='validate_documento'),
    url(r'^ajax/validate_email/$', login_views.validate_email, name='validate_email'),
]
