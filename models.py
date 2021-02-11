from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=500)
	image = models.ImageField(upload_to='profile_pic/')

	def __str__(self):
		return self.description

class Comment(models.Model):
	profile_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_user')
	text = models.TextField()
	date = models.DateTimeField(default= timezone.now)

	def __str__(self):
		return self.profile_user.user.username

class Blog(models.Model):
	title_text = models.CharField(max_length=255, null=True)
	main_text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
	audience = models.ManyToManyField(User, related_name='blog_audience')
	date = models.DateTimeField(default= timezone.now)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

	def datepublished(self):
		return self.date.strftime('%Y %B %d')

	def __str__(self):
		if(self.title_text != None):
			return self.title_text
		else:
			return self.main_text
