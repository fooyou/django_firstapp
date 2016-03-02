#!/usr/bin/env python
# coding: utf-8
# @File Name: hello.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-03-02 09:03:48
# @Last Modified: 2016-03-02 11:03:31
# @Description:
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
        }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "问题答案 %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("为问题投票 %s." % question_id)

