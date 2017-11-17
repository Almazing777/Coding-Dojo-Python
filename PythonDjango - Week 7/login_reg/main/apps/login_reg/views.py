from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from .models import *

def index(request):
	    return render(request, "login_reg/index.html")

def register(request):
	result = User.objects.validate_registration(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect ('/')
	request.session["email"] = result.email
	return redirect('/success')

def login(request):
	result = User.objects.validate_login(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect ("/")
	request.session["email"] = result.email
	return redirect ('/success')

def success(request):
	try:
		request.session["email"]
	except KeyError:
		return redirect('/')
	context = {
		"user": User.objects.get(email=request.session["email"])
	}
	return render(request, "login_reg/success.html")



