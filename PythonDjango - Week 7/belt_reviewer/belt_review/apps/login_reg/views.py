from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages

def index(request):
	    return render(request, "login_reg/index.html")

def register(request):
	result = User.objects.validate_registration(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect ('/')
	request.session["user_id"] = result.id
	return redirect(reverse('review:index'))

def login(request):
	result = User.objects.validate_login(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect ("/")
	request.session["user_id"] = result.id
	return redirect(reverse('review:index'))

def logout(request):
	request.session.clear()
	return redirect ('/')


