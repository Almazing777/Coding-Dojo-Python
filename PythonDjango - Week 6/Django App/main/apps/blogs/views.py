from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	response = "placeholder to later display all the list of blogs - this our first request"
	return HttpResponse(response)

def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect ('/')

def show(request, number):
	return HttpResponse("placeholder to display blog " + number)

def edit(request, number):
	return HttpResponse("placeholder to display edit " + number)

def destroy(request, number):
	return redirect ('/')

	
# def show(request, number):
# 	print number
# 	return HttpResponse("show method" + number)

# def show_word(request, word):
# 	return HttpResponse("show_word method" + word)

# def year_archive(request, year):
# 	return HttpResponse("year_archive method" + year)

# def month_archive(request, year, month):
# 	return HttpResponse("month_archive method" + year)