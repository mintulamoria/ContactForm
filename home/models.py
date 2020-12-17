from django.db import models
from django.utils import timezone
#from django.conf import settings


class Contact(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	mobile_number = models.IntegerField()
	message = models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def full_name(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def __str__(self):
		return self.full_name()