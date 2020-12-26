"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet
from snippets import views
from idcs.views import idc_list
# from snippets.views import snippet_list, snippet_detail
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^snippets/$', views.SnippetList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^idcs/$', idc_list),
    # url(r'^snippets/(?P<pk>[0-9]+)$', snippet_detail),
    url(r'^admin/', admin.site.urls),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
