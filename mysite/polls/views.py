from django.shortcuts import render

from django.http import HttpResponse

from .models import Question



# Create your views here.
def index(request):
	#all_question_objects = Question.objects.order_by("-pub_date")
	all_question_objects = Question.objects.all()
	list_of_questions = [q.question_text for q in all_question_objects]
	output = "<br><br>".join(list_of_questions)
	return HttpResponse(output)
	#return HttpResponse("Aha ! this comes from Polls->index")


def detail(request, question_id):
	response = "You are looking at question %s"
	return HttpResponse(response % question_id)

def results(request, question_id):
	response = "You are viewing results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	response = "You are viewing Vote panel of question %s"
	return HttpResponse(response % question_id)
