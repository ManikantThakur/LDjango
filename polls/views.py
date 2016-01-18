from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hello, we are in index.')


def details(request, question_id):
    return HttpResponse("You are looking details of question# %s" % question_id)


def results(request, question_id):
    response = "You are looking the result of question# %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question# %s" % question_id)

