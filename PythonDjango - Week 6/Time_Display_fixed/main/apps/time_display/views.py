from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *

def index(request):
	context = {
		"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
	}
	return render(request, 'time_display/index.html', context)
