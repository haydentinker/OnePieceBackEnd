from onepiece.models import Character
import csv

def run():
    with open('onepiece/scripts/data/character.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Character.objects.all().delete()

        for row in reader:
            print(row)
            if row[2] != '':
                new_character = Character(url=row[0],
                            name=row[1],
                            anime_debut=row[2], 
                            affiliations=row[3],
                            occupations=row[4],
                            birthday=row[5])
            new_character.save()