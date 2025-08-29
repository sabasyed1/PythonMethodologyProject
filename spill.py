# spill.py

import csv
from collections import Counter
from datetime import datetime

# Constants
DATA_FILE = '/Users/sabasyed/Desktop/Final Python/spill_incidents.csv'

# Class of spill 
class Spill:
    def __init__(self, date, county, substance):
        self.date = date
        self.county = county
        self.substance = substance

# Using inheritance
class OilSpill(Spill):
    def __init__(self, date, county, volume):
        super().__init__(date, county, 'Oil')
        self.volume = volume

# Function to read spills from the csv file and returns data
def load_spill_data(filepath):
    county_counter = Counter()
    substance_counter = Counter()
    spills = []

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            county = row.get('County', '').strip().title()
            substance = row.get('Material Name', '').strip().title()
            date_str = row.get('Spill Date', '').strip()

            if not (county and substance and date_str):
                continue

            try:
                date = datetime.strptime(date_str, '%m/%d/%Y')
                spill = Spill(date, county, substance)
                spills.append(spill)
                county_counter[county] += 1
                substance_counter[substance] += 1
            except Exception:
                continue

    return spills, county_counter, substance_counter

# Function to save the summary report
def save_summary(county_counts, substance_counts, filepath):
    with open(filepath, 'w') as f:
        f.write("The Top 5 Counties by Spill Count:\n")
        for county, count in county_counts.most_common(5):
            f.write(f"- {county}: {count} spills\n")
        f.write("\nThe Top 5 Material Spilled:\n")
        for substance, count in substance_counts.most_common(5):
            f.write(f"- {substance}: {count} spills\n")
