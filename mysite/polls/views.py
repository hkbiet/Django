from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(index):
	return HttpResponse("Aha ! this comes from Polls->index")