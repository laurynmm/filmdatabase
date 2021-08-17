from django.test import TestCase

from catalog.models import Film

# Film tests
class TestFilmModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create film
        Film.objects.create(title='My Dinner with Andre', year=1981)

    def test_film_title_max_length(self):
        test_film = Film.objects.get(id=1)
        expected = 200
        returned = test_film._meta.get_field('title').max_length
        self.assertEqual(returned, expected)

    def test_object_string_is_title(self):
        test_film = Film.objects.get(id=1)
        expected = 'My Dinner with Andre'
        self.assertEqual(str(test_film), expected)

    def test_get_absolute_url(self):
        test_film = Film.objects.get(id=1)
        # Needs views and urls to be configured to pass
        self.assertEqual(test_film.get_absolute_url(), '/catalog/film/1')
