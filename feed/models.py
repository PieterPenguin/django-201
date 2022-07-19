from django.contrib.auth.models import User
from django.db import models
from django.forms import ImageField


class Post(models.Model):
	title = models.CharField(max_length=40)
	text = models.CharField(max_length=140)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	file = models.FileField(upload_to='media/media/files')


	def __str__(self) -> str:
		return self.text

