from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def index1(request):
    return HttpResponse("АБОБУС")
def detail(request, question_id):
    Choice_list = Choice.objects.order_by('-pub_date')[:5]
    context = {'Choice_list': Choice_list}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
