import csv
from models.city import City
from models.map import Map

file_path = "C:\\Users\\futbo\\Desktop\\homework\\src\\data\\city_data.csv"
cities_map = Map()

def read_csv(file_path: str) -> None:
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            temp = City(city_name=row[0], lat=float(row[1]), lng=float(row[2]), country=row[3], iso2=row[4], population=float(row[7]))
            cities_map.add_city(temp)

# Call the function to read the CSV file and populate the cities_map
read_csv(file_path)

# The rest of the main.py will be handled in the PyQt interface
