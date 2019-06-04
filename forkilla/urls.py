from django.conf.urls import url

from . import views

listOfAddresses = ["161.116.56.65","161.116.56.165"] # Rellenar con direcciones ip

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^restaurant/(?P<restaurant_number>.*)/review$', views.add_comment, name='review'),
    url(r'^register/$', views.register, name='register'),
    url(r'^restaurants/$', views.restaurants, name='restaurants'),
    url(r'^restaurants/(?P<city>.*)/$', views.restaurants, name='restaurants'),
    url(r'^restaurants/(?P<city>.*)/(?P<category>.*)$', views.restaurants, name='restaurants'),
    url(r'^restaurant/(?P<restaurant_number>.*)/', views.details, name='details'),
    url(r'^reservation/$', views.reservation, name='reservation'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^reservation_list/$', views.reservation_list, name='reservation_list'),
    url(r'^delete_reservation/$', views.delete_reservation, name='delete_reservation'),
    url(r'^comparator$', views.comparator, name='comparator'),
]
