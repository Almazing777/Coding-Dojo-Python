from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
	return render(request, "amadon/index.html")

def buy(request):
	product_id = request.POST['product_id']
	quantity = request.POST['quantity']

	if (product_id == "1015"):
		price = 19.99
	elif (product_id == "1016"):
		price = 29.99
	elif (product_id == "1017"):
		price = 4.99
	elif (product_id == "1018"):
		price = 49.99
	else:
		price = 0

	total_amount = int(quantity) * price

	try:
		request.session["times"] += int(quantity)
		request.session["charged_amount"] = total_amount
		request.session["spent"] +=total_amount
	except:
		request.session["num_items"] = int(quantity)
		request.session["charged_amount"] = total_amount
		request.session["spent"] = total_amount

	return render(request, "amadon/checkout.html")

def back(request):
	return redirect ('/')

