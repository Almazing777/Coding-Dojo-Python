from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):

	context = {
		'recent': Review.objects.recent_and_not()[0],
		'more': Review.objects.recent_and_not()[1]
	}
	return render(request, "belt/index.html", context)

def add(request):
	context = {
		'authors': Author.objects.all()
	}
	return render(request, "belt/add.html", context)

def show(request, book_id):
	context = {
		'book': Book.objects.get(id=book_id)
	}
	return render(request, 'belt/show.html', context)

def create(request):
	errs = Review.objects.validate_review(request.POST)
	if errs:
		for e in errs:
			message.error(request, e)
	else:
		book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
 	return redirect('/books/')

def create_additional(request, book_id):
	the_book = Book.objects.get(id=book_id)
	new_book_data = {
		"title": the_book.title,
		"author": the_book.author.id,
		"rating": request.POST["rating"],
		"review": request.POST["review"],
		"new_author": ""
	}
	errs = Review.objects.validate_review(new_book_data)
	if errs:
		for e in errs:
			message.error(request, e)
	else:
		Review.objects.create_review(new_book_data, request.session["user_id"])
	return redirect("/books/")

def delete_review(request, review_id):
	review = Review.objects.get(id=review_id)
	book_id = review.book.id
	if (review.user.email == request.session['user_email']): 
		review = Review.objects.delete_review(review_id)

	return redirect('/books/{}'.format(book_id))

def show_user(request, user_id):
	user = User.objects.get(id=user_id)
	reviews = user.reviews.all()
	books = []
	for review in reviews:
		if review.book not in books:
			books.append(review.book)
	context = {
		"user": user,
		"num_reviews": len(reviews),
		"books": books	
	}
	return render(request, "belt/userinfo.html", context)

