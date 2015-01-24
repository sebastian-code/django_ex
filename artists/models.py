from django.db import models

class Artist(models.Model):
	"""docstring for Artist"""
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	biography = models.TextField(blank=True)

	def __unicode__(self):
		return self.first_name