from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
	def basic_validator(self, post_data):
		errors = []
		if len(post_data["course_name"]) < 5:
			errors["course_name"] = "Name field must be 5 characters or more"
		if len(post_data["desc"]) < 15:
			errors["desc"] = "Description field must be 15 characters or more"
		return errors


class Course(models.Model):
	course_name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()

