from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *

def index(request):
	context = {
		"all_courses": Course.objects.all()
	}
	return render(request, "courses/index.html", context)

def create(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
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

# def new(request):
# 	return render(request, 'users/new.html')

# def edit(request, user_id):
# 	context = {
# 		'user': User.objects.get(id=user_id)
# 	}
# 	return render(request, 'users/update.html', context)

# def update(request, user_id):
# 	if request.method == "POST":
# 		user_to_update = User.objects.get(id=user_id)
# 		user_to_update.first_name = request.POST["first_name"]
# 		user_to_update.last_name = request.POST["last_name"]
# 		user_to_update.email = request.POST["email"]
# 		user_to_update.save()
# 		return redirect ('/')
# 	else:
# 		context = {
# 			"user": User.objects.get(id=user_id)
# 		}
# 		return render(request, "users/show.html", context)


