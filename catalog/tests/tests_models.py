import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from catalog.models import Genre, Language, Person, Film, Review

# Genre tests
class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Documentary')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        expected = 200
        returned = genre._meta.get_field('name').max_length
        self.assertEqual(returned, expected)

    def test_name_help_text(self):
        genre = Genre.objects.get(id=1)
        expected = 'Enter a film genre (e.g. Noir)'
        returned = genre._meta.get_field('name').help_text
        self.assertEqual(returned, expected)

    def test_object_string_is_name(self):
        genre = Genre.objects.get(id=1)
        expected = 'Documentary'
        self.assertEqual(str(genre), expected)

# Language tests
class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Spanish')

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        expected = 100
        returned = language._meta.get_field('name').max_length
        self.assertEqual(returned, expected)

    def test_name_help_text(self):
        language = Language.objects.get(id=1)
        expected = 'Enter primary language of film (e.g. French)'
        returned = language._meta.get_field('name').help_text
        self.assertEqual(returned, expected)

    def test_object_string_is_name(self):
        language = Language.objects.get(id=1)
        expected = 'Spanish'
        self.assertEqual(str(language), expected)

# Person tests
class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(first_name='Tilda', last_name='Swinton')

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'date of death')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        expected = 100
        max_length = person._meta.get_field('first_name').max_length
        self.assertEqual(max_length, expected)

    def test_last_name_max_length(self):
        person = Person.objects.get(id=1)
        expected = 100
        max_length = person._meta.get_field('last_name').max_length
        self.assertEqual(max_length, expected)

    def test_object_string_is_last_name_comma_first_name(self):
        person = Person.objects.get(id=1)
        expected = 'Swinton, Tilda'
        self.assertEqual(str(person), expected)

    def test_get_absolute_url(self):
        person = Person.objects.get(id=1)
        # Needs views and urls to be configured to pass
        self.assertEqual(person.get_absolute_url(), '/catalog/person/1')

# Film tests
class TestFilmModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create genre & language
        test_genre = Genre.objects.create(name='Comedy')
        test_language = Language.objects.create(name='English')

        # Create film
        Film.objects.create(
            title='My Dinner with Andre',
            plot='Two old friends meet for dinner; as one tells anecdotes detailing his experiences, the other notices their different world views.',
            year=1981,
            imdb_id='tt0082783',
            language=test_language,
        )

        # add genre as post step
        Film.objects.get(id=1).genre.add(test_genre)
        Film.objects.get(id=1).save()

    def test_film_title_max_length(self):
        test_film = Film.objects.get(id=1)
        expected = 200
        returned = test_film._meta.get_field('title').max_length
        self.assertEqual(returned, expected)

    def test_film_plot_max_length(self):
        test_film = Film.objects.get(id=1)
        expected = 1000
        returned = test_film._meta.get_field('plot').max_length
        self.assertEqual(returned, expected)

    def test_plot_help_text(self):
        test_film = Film.objects.get(id=1)
        expected = 'Enter a brief description of the film'
        returned = test_film._meta.get_field('plot').help_text
        self.assertEqual(returned, expected)

    def test_object_string_is_title(self):
        test_film = Film.objects.get(id=1)
        expected = 'My Dinner with Andre'
        self.assertEqual(str(test_film), expected)

    def test_get_absolute_url(self):
        test_film = Film.objects.get(id=1)
        # Needs views and urls to be configured to pass
        self.assertEqual(test_film.get_absolute_url(), '/catalog/film/1')

# Review tests
class TestReviewModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create genre & language
        test_genre = Genre.objects.create(name='Comedy')
        test_language = Language.objects.create(name='English')

        # Create film
        Film.objects.create(
            title='My Dinner with Andre',
            plot='Two old friends meet for dinner; as one tells anecdotes detailing his experiences, the other notices their different world views.',
            year=1981,
            imdb_id='tt0082783',
            language=test_language,
        )

        # add genre as post step
        Film.objects.get(id=1).genre.add(test_genre)
        Film.objects.get(id=1).save()

        # Create user
        test_user = User.objects.create(username='testuser', password='1z!Z2a@A')
        test_user.save()

    def test_object_string_is_rating_of_film_by_user(self):
        test_review = Review.objects.create(
            user=User.objects.get(id=1),
            film=Film.objects.get(id=1),
            rating=3,
        )
        expected = 'Good rating of My Dinner with Andre by testuser'
        self.assertEqual(str(test_review), expected)
