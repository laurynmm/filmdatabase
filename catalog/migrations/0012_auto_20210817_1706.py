# Generated by Django 3.2.6 on 2021-08-17 15:06
import csv

from django.db import migrations

def add_films(apps, schema_editor):
    Film = apps.get_model('catalog', 'Film')
    with open('/home/lauryn/DataScience/Python/django_projects/filmdatabase/data/test_data.csv', newline='') as data:
        reader = csv.reader(data)
        next(reader)
        films = []
        for row in reader:
            films.append(Film(title=row[1], year=int(row[3][:4])))
        Film.objects.bulk_create(films)
            
class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_film_year'),
    ]

    operations = [
        migrations.RunPython(add_films)
    ]