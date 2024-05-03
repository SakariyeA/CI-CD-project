import csv
import json

def konvertera_csv_till_json(csv_fil, json_fil):
    # Öppna CSV-filen och läs innehållet
    with open(csv_fil, 'r') as csvfile:
        # Skapa en CSV-läsare
        csvläsare = csv.DictReader(csvfile)


        data = []
        for rad in csvläsare:
            data.append(rad)


    with open(json_fil, 'w') as jsonfil:
        json.dump(data, jsonfil, indent=4)


konvertera_csv_till_json('profiles1.csv', 'nydata.json')