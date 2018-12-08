from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^StepsRequired$', views.steps, name="steps"),
    url(r'^Login$', views.login, name="Login"),
    url(r'^seltype/(?P<cardnum>[\w-]+)/$', views.seltype, name="seltype"),
    url(r'^mysettings$', views.set, name="set"),
    url(r'^transact/(?P<cardnum>[\w-]+)/$', views.transact, name="transact"),
    url(r'^withdraw/(?P<cardnum>[\w-]+)/$', views.withdraw, name="withdraw"),
    url(r'^enquire/(?P<cardnum>[\w-]+)/$', views.enquire, name="enquire"),
    url(r'^deposit/(?P<cardnum>[\w-]+)/$', views.deposit, name="deposit"),
]
