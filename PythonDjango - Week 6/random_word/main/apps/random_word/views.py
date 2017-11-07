from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if "times" in request.session:
		request.session['times'] +=1
	else:
		request.session["times"] = 1

	context = {
		"random_word": get_random_string(length=14),
		"times": request.session['times']
	}
	return render(request, 'random_word/index.html', context)

def reset(request):
	del request.session['times']
	del request.session['word']
	return redirect('/')
