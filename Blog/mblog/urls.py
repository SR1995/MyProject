"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('',views.index.as_view(),name='index'),#views.index,name='index'  IndexView.as_view
	path('type=<str:type>',views.Type_search.as_view(),name='type_search'),
	path('type=<str:type>/Article=<str:ArticleName>',views.Show_Article.as_view(),name='show_Article'),
	path('search',views.serach.as_view(),name='search')
	#path('ckeditor/',include('ckeditor_uploader.urls')),
]
