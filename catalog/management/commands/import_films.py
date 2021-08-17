import csv

from django.core.management import BaseCommand

from catalog.models import Film

class Command(BaseCommand):
  help = "Imports film information from csv file."

  def add_arguments(self, parser):
    parser.add_argument("file_path", type=str)

  def handle(self, *args, **options):
    file_path = options["file_path"]
    with open(file_path, newline='') as data:
        reader = csv.reader(data)
        next(reader)
        films = []
        for row in reader:
            films.append(Film(title=row[1], year=int(row[3][:4])))
        count = 0
        for film in films:
          obj, created = Film.objects.get_or_create(title=film.title, year=film.year)
          if created:
            count += 1

    self.stdout.write(self.style.SUCCESS(f'From {len(films)} rows in csv, there were {count} films added to database'))
