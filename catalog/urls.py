from django.urls import path, re_path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^fighters/$', views.FighterViewList.as_view(), name='fighters'),
    re_path(r'^fighter/(?P<pk>\d+)$', views.FighterViewDetail.as_view(), name='fighter-detail')
]