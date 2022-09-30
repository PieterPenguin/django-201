from django.contrib.auth.models import User
from django.db import models
from django import forms


class Post(models.Model):
	title = models.CharField(max_length=40)
	text = models.CharField(max_length=140)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)


	def __str__(self) -> str:
		return self.text


	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args, **kwargs)



class FileFolder(models.Model):
   files = {"": ""}
