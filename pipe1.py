import csv
import json

# Define the input CSV file and output JSON file
csv_file = '/Users/saisarathkanamarlapudi/Documents/ZipCodeWilmington/PipelineOne/timecard_data.csv'
json_file = '/Users/saisarathkanamarlapudi/Documents/ZipCodeWilmington/PipelineOne/timecard_data.json'

# Read the CSV file and calculate the total gross pay
timecard_data = []
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row['name']
        hours_worked = float(row['hours_worked'])
        hourly_rate = float(row['hourly_rate'])
        bonus = float(row['bonus'])
        gross_pay = hours_worked * hourly_rate + bonus
        timecard_data.append({
            'name': name,
            'hours_worked': hours_worked,
            'hourly_rate': hourly_rate,
            'bonus': bonus,
            'gross_pay': gross_pay
        })

# Write the data to a JSON file
with open(json_file, mode='w') as file:
    json.dump(timecard_data, file, indent=4)

print("Data has been successfully written to", json_file)

