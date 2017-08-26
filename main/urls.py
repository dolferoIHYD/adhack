from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<slug>[-a-z-A-Z-а-я-А-Я-0-9-_+.]+)/$', views.landing_view),

]
