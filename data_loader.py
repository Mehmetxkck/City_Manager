import csv



def load_city_data(file_path):
    file_path="C:\\Users\\futbo\\Desktop\\homework\\src\\data\\city_data.csv"
    cities = []

    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                if len(row) == 9:
                    city = city(row[0], float(row[1]), float(row[2]), row[3], row[4], row[5], row[6], int(row[7]), int(row[8]))
                    cities.append(city)
                else:
                    print(f"Ignoring invalid data: {row}")

        return cities
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
file_path = "C:\\Users\\futbo\\Desktop\\homework\\src\\data\\city_data.csv"
cities = load_city_data(file_path)

for city in cities:
    city.display_info()
    print("-----------------")