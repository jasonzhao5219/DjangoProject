from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    #url(r'^process$', views.process),
    #url(r'^show$', views.show),
    #url(r'^add$', views.add),
    #url(r'^addshow$', views.addshow),
    #url(r'^addfavorite/(?P<number>\d+)$', views.addfavorite),
    #url(r'^removefavorite/(?P<number>\d+)$', views.removefavorite),
    #url(r'^iteminfo/(?P<number>\d+)$', views.iteminfo),
    #url(r'^dashboard$', views.dashboard),
    #url(r'^logout$', views.logout),
    #url(r'^login$', views.login),
    #url(r'^itemdelete/(?P<number>\d+)$', views.itemdelete)
    url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard),
    url(r'^order$', views.order),
    url(r'^process$', views.process),
    url(r'^register$', views.register),
    url(r'^process/(\w+)$', views.process),
    url(r'^checkout$', views.checkout),
    url(r'^charge$', views.charge),
    url(r'^admin$', views.admin_users),
    url(r'^admin/coders$', views.admin_coders),
    url(r'^coders/remove/(?P<number>\d+)$', views.remove_coder),
    url(r'^logout$', views.logout),
    url(r'^coder_profile/(?P<number>\d+)$', views.coder_profile),
]