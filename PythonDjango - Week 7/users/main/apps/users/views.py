from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *

def index(request):
	if request.method == "POST":
		print request.POST
		User.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"])
		return redirect ('/')
	else: 
		context = {
			"all_users": User.objects.all()
		}
		return render(request, "users/index.html", context)

def new(request):
	return render(request, 'users/new.html')

def edit(request, user_id):
	context = {
		'user': User.objects.get(id=user_id)
	}
	return render(request, 'users/update.html', context)

def update(request, user_id):
	if request.method == "POST":
		user_to_update = User.objects.get(id=user_id)
		user_to_update.first_name = request.POST["first_name"]
		user_to_update.last_name = request.POST["last_name"]
		user_to_update.email = request.POST["email"]
		user_to_update.save()
		return redirect ('/')
	else:
		context = {
			"user": User.objects.get(id=user_id)
		}
		return render(request, "users/show.html", context)

def delete(request, user_id):
	user_to_delete = User.objects.get(id=user_id).delete()
	return redirect ('/')

