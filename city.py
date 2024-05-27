class City:
    def __init__(self, city_name : str, country: str, lng: float, lat: float, iso2: str, population: float):
        self.city_name = city_name
        self.lat = lat
        self.lng = lng
        self.country = country
        self.iso2 = iso2
        self.population = population

    def display_info(self):
        print(f"City: {self.city_name}")
        print(f"Latitude: {self.lat}")
        print(f"Longitude: {self.lng}")
        print(f"Country: {self.country}")
        print(f"Iso2: {self.iso2}")
        print(f"Population: {self.population}")