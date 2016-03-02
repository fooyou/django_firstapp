#!/usr/bin/env python
# coding: utf-8
# @File Name: urls.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-03-02 09:03:39
# @Last Modified: 2016-03-02 15:03:34
# @Description:
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
        # 例如： /polls/
        url(r'^$', views.IndexView.as_view(), name='index'),
        # 例如： /polls/5/
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        # 例如： /polls/5/results/
        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        # 例如： /polls/5/vote/
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    ]
