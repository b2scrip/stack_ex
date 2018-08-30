"""btcfaq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.flatpages import views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from post.views import  RootPage,Home,Detail,Price
from eos.views import  EosHome,EosDetail
from eth.views import  EthHome,EthDetail

from eos.models import Question as eosqn
from eth.models import Question as ethqn
from post.models import Question as btcqn


info_dict = {
    'queryset': eosqn.objects.all(),
    'date_field': 'creationdate',
}

info2_dict = {
    'queryset': btcqn.objects.all(),
    'date_field': 'creationdate',
}

info3_dict = {
    'queryset': ethqn.objects.all(),
    'date_field': 'creationdate',
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path('price/<str:type>/', Price.as_view(),name="coin_price"),

    path('', RootPage.as_view()),
    path('btc/', Home.as_view()),
    path('detail/<int:pk>/', Detail.as_view(),name="btc_detail"),

    path('eos/', EosHome.as_view()),
    path('eos/detail/<int:pk>/', EosDetail.as_view(),name="eos_detail"),

    path('eth/', EthHome.as_view()),
    path('eth/detail/<int:pk>/', EthDetail.as_view(),name="eth_detail"),

    path('eth/sitemap.xml', sitemap,
         {'sitemaps': {'eth': GenericSitemap(info3_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap.eos'),
    path('eos/sitemap.xml', sitemap,
         {'sitemaps': {'eos': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap.eos'),
    path('btc/sitemap.xml', sitemap,
         {'sitemaps': {'btc': GenericSitemap(info2_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap.btc'),
    path('license/', views.flatpage, {'url': '/license/'}, name='license'),
]
