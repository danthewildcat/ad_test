"""ad_test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from tastypie.api import Api

from shopping.api import ListItemResource, ShoppingListResource
from views import create_user, index, profile

v1_api = Api(api_name='v1')
v1_api.register(ShoppingListResource())
v1_api.register(ListItemResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    
    url(r'^create_user$', create_user, name='create_user'),
    url(r'^profile$', login_required(profile), name='profile'),
    
    url('^accounts/', include('django.contrib.auth.urls')),
    
    url(r'^api/', include(v1_api.urls)),
]
