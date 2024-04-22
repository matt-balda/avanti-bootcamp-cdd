import requests
import csv

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/exercise.csv"
response = requests.get(url)

if response.status_code == 200:
    csv_data = response.text

    new_path = "../../data/raw/exercise.csv"

    with open(new_path, "w", newline="") as csv_file:
        csv_file.write(csv_data)

    print("Csv saved successfully")
else:
    print("Failed to download data", response.status_code)