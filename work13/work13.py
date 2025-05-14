# Городецький А.Ю.
import csv
import json
import os

# Дані студентів
countries = [
    {"Name": "Ukraine", "Area": 603628, "Population": 41000000, "Continent": "Europe"},
    {"Name": "Nigeria", "Area": 923768, "Population": 206000000, "Continent": "Africa"},
    {"Name": "China", "Area": 9596961, "Population": 1400000000, "Continent": "Asia"},
]

csv_filename = 'countries.csv'
json_filename = 'countries.json'

# Створення .csv файлу та запис у нього
try:
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Area', 'Population', 'Continent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in countries:
            writer.writerow(student)
    print(f"Файл '{csv_filename}' успішно створено")
except IOError as e:
    print(f"Помилка запису у CSV файл: {e}")

# Зчитування з .csv та конвертація у .json
try:
    with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
    print(f"Файл '{json_filename}' успішно створено")
except FileNotFoundError:
    print(f"Файл '{csv_filename}' не знайдено.")
except json.JSONDecodeError as e:
    print(f"Помилка конвертації JSON: {e}")
except IOError as e:
    print(f"Помилка читання або запису файлу: {e}")

