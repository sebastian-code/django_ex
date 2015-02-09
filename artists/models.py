from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	biography = models.TextField(blank=True)
	favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name='faved_by')

	def es_pharrel(self):
		return self.id == 1

	@staticmethod
	def autocomplete_search_fields():
		return ("id_iexact", "first_name__icontains", "last_name__icontains")

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)