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

from views import create_user, index, list_item, profile, shopping_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    
    url(r'^create_user$', create_user, name='create_user'),
    url(r'^profile$', login_required(profile), name='profile'),
    
    url(r'^shopping$', login_required(shopping_list)),
    url(r'^shopping/(?P<pk>\d+)$', login_required(shopping_list)),
    
    url(r'^item$', login_required(list_item)),
    url(r'^item/(?P<pk>\d+)$', login_required(list_item)),
    
    url('^accounts/', include('django.contrib.auth.urls'))
]
