from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import *

def index(request):
	context = {
		"all_courses": Course.objects.all()
	}
	return render(request, "courses/index.html", context)

def create(request):
	result = Course.objects.basic_validator(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect('/')
	else:
		Course.objects.create(course_name = request.POST["course_name"], desc = request.POST["desc"])
		return redirect ('/')	

def delete(request, course_id):
	course_to_delete = Course.objects.get(id=course_id).delete()
	return redirect ('/')

def confirm(request, course_id):
	context = {
		"course": Course.objects.get(id=course_id)
	}
	return render(request, 'courses/confirm.html', context)


