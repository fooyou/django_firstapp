#!/usr/bin/env python
# coding: utf-8
# @File Name: hello.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-03-02 09:03:48
# @Last Modified: 2016-03-02 10:03:19
# @Description:
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '\n'.join([q.question_text for q in last_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("请看问题 %s." % question_id)

def results(request, question_id):
    response = "问题答案 %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("为问题投票 %s." % question_id)

