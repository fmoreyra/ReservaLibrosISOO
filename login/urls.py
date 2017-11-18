from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from login import views as login_views
from reserva import views as reserva_views

urlpatterns = [
    url(r'^$', reserva_views.ReservaQuery, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', login_views.signup, name='signup'),
    url(r'^ajax/validate_username/$', login_views.validate_username, name='validate_username'),
    url(r'^ajax/validate_legajo/$', login_views.validate_legajo, name='validate_legajo'),
    url(r'^ajax/validate_documento/$', login_views.validate_documento, name='validate_documento'),
    url(r'^ajax/validate_email/$', login_views.validate_email, name='validate_email'),
    url(r'^profile/$', login_views.profile_search, name='profile_search'),
    url(r'^profile/(?P<pk>\d+)$', login_views.ProfileDetailView.as_view(), name='profile_detail'),
    url(r'^libro/$', login_views.libro_search, name='libro_search'),
    url(r'^libro/(?P<pk>\d+)$', reserva_views.LibroDetailView.as_view(), name='libro_detail'),
    url(r'^reserva/$', reserva_views.CreateReserva, name='create_reserva'),
    url(r'^admin_view/$', reserva_views.AdminQuery, name='admin_view'),
    url(r'^reserva/(?P<pk>\d+)/delete/$', reserva_views.DeleteReserva.as_view(), name='delete_reserva'),
]
