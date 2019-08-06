"""TestShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
#from django.contrib import admin
import xadmin
from TestShop.settings import MEDIA_ROOT
from  django.views.static import serve
from rest_framework.authtoken import views

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet,CategoryViewSet

router=DefaultRouter()

router.register(r'goods',GoodsListViewSet,base_name='goods')

router.register(r'categorys',CategoryViewSet,base_name='category')



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    #获取token的
    url(r'^get_token-auth/', views.obtain_auth_token),

    #rest_framework的配置
    url(r'^docs/',include_docs_urls(title="生鲜")),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #router的配置
    url(r'^',include(router.urls)),
]
