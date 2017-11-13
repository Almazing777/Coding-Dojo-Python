from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

def index(request):
    return HttpResponse("Go make some shell queries!")
	