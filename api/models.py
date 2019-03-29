from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=64)
	description =  models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)