from django.conf.urls import url
from . import views

app_name = 'Wine'

urlpatterns = [
    # /
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /winery_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # winery/add/
    url(r'^winery/add/$', views.WineryCreate.as_view(), name='winery-add'),

    # winery/update/
    url(r'^winery/(?P<pk>[0-9]+)/$', views.WineryUpdate.as_view(), name='winery-update'),

    # winery/delete
    url(r'^winery/(?P<pk>[0-9]+)/delete/$', views.WineryDelete.as_view(), name='winery-delete'),

    # winery/addcollection
    url(r'^winery/addcollection/$', views.AddCollection.as_view(), name='winery-add-collection')

    # # /winery/winery_id/favorite/
    # url(r'^(?P<winery_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
