from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def validate_login(self, postData):
		errors = []
		if len(self.filter(email=postData["email"])) > 0:
			user = self.filter(email=postData["email"])[0]
			if not bcrypt.checkpw(postData["password"].encode(), user.password.encode()):
				errors.append("email/password incorrect")
		else:
			errors.append("email/password incorrect")

		if errors:
			return errors
		return user

	def validate_registration(self,postData):
		errors = []
		if len(postData["first_name"]) <2:
			errors.append("First name can't be fewer than 2 characters")
		if len(postData["last_name"]) <2:
			errors.append ("Last Name must be atleast 2 characters long")
		if len(postData["email"]) < 1:
			errors.append("Email can't be blank")

		if not re.match(EMAIL_REGEX, postData["email"]):
			errors.append("Email invalid")

		if len(User.objects.filter(email = postData["email"])) > 0:
			errors.append("Email already in use")

		if len(postData["password"]) < 8:
			errors.append("Password can't be less than 8 characters long")

		if postData["password"] != postData["confirm_password"]:
			errors.append("Passwords do not match")

		if not errors:
			first_name = postData["first_name"]
			last_name = postData["last_name"]
			email = postData["email"]
			password_raw = postData["password"]
			password_hash = bcrypt.hashpw(password_raw.encode(), bcrypt.gensalt())
			User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password_hash)
			errors.append("Succesful Regsitration")
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	confirm_password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def display_info(self):
		print self.email
		print self.password

