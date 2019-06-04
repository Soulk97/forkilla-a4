"""PracticaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from forkilla import views


# API
router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, base_name='Restaurants')

urlpatterns = [
    url(r'^forkilla/', include('forkilla.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$',  login,  name='login'),
    url(r'^accounts/logout/$',  logout,  {'next_page': '/forkilla'}, name='logout'),
    url(r'^$', include('forkilla.urls')),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

#handler404 = 'forkilla.views.handler404'
#handler500 = 'forkilla.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
