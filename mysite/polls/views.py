from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(index):
	return HttpResponse("Aha ! this comes from Polls->index")


def detail(request, question_id):
	response = "You are looking at question %s"
	return HttpResponse(response % question_id)

def results(request, question_id):
	response = "You are viewing results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	response = "You are viewing Vote panel of question %s"
	return HttpResponse(response % question_id)
