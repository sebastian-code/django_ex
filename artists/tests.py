from django.test import TestCase

from .models import Artist
# Create your tests here.
class TestArtist(TestCase):

	def setUp(self):
		self.artist = Artist.object.create(first_name='David', last_name='Bowie')


	def test_existe_vista(self):
		res = self.client.get('/artist/%d/' % self.artist.id)
		self.assertEqual(res.status_code, 200)
		self.assertTrue('David' in res.content)

	def test_no_existe_vista(self):
		id_viejo = self.artist.id
		self.artist.delete()
		res = self.client.get('/artist/%d/' % id_viejo)
		self.assertEqual(res.status_code, 404)