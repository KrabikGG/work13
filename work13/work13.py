# Городецький А.Ю.
import csv
import json
import os

countries = [
    {"Name": "Ukraine", "Area": 603628, "Population": 41000000, "Continent": "Europe"},
    {"Name": "Nigeria", "Area": 923768, "Population": 206000000, "Continent": "Africa"},
    {"Name": "China", "Area": 9596961, "Population": 1400000000, "Continent": "Asia"},
]

# Коваль А.М.
# Додаткові країни
additional_countries = [
    {"Name": "Brazil", "Area": 8515767, "Population": 213000000, "Continent": "South America"},
    {"Name": "Canada", "Area": 9984670, "Population": 38000000, "Continent": "North America"},
]

countries.extend(additional_countries)

csv_filename = 'countries.csv'
json_filename = 'countries.json'
csv_from_json_filename = 'countries_from_json.csv'

try:
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Area', 'Population', 'Continent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for country in countries:
            writer.writerow(country)
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

# Зчитування з .json і запис назад у CSV
try:
    with open(json_filename, mode='r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)

    with open(csv_from_json_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Area', 'Population', 'Continent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for country in json_data:
            writer.writerow(country)
    print(f"Файл '{csv_from_json_filename}' успішно створено з JSON-даних")
except FileNotFoundError:
    print(f"Файл '{json_filename}' не знайдено.")
except json.JSONDecodeError as e:
    print(f"Помилка читання JSON: {e}")
except IOError as e:
    print(f"Помилка запису у CSV з JSON: {e}")
