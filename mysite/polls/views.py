#!/usr/bin/env python
# coding: utf-8
# @File Name: hello.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-03-02 09:03:48
# @Last Modified: 2016-03-02 15:03:08
# @Description:
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        ''' 返回最近的5个问题 '''
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            '错误消息：': "没有选择答案"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        cat_str = reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(cat_str)

