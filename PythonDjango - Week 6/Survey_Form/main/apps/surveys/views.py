from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
	return render(request, 'surveys/index.html')

def process(request):
	if "times" in request.session:
		request.session['times'] +=1
	else:
		request.session["times"] = 1

	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	return redirect ('/result')

def result(request):
	return render(request, "surveys/results.html")

def back(request):
	return redirect ('/')