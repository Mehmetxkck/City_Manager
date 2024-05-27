from .city import City
import folium
import os

class Map:
    def __init__(self):
        self.cities_map: list[City] = []

    def display_city_info(self, city: str) -> City:
        found_city = next((c for c in self.cities_map if c.city_name.lower() == city.lower()), None)
        return found_city


    def add_city(self, city_to_add: City) -> None:
        """Add a city to the map."""
        self.cities_map.append(city_to_add)

    def display_all_cities(self) -> str:
        all_cities_info = ""
        for city in self.cities_map:
            all_cities_info += f"City: {city.city_name}, Population: {city.population}\n"
        return all_cities_info



    def generate_city_map(self, city_name: str) -> None:
        """Generate a map for the entered city."""
        city = next((c for c in self.cities_map if c.city_name.lower() == city_name.lower()), None)
        if city:
            # Create the directory if it doesn't exist
            directory = "assets/cities"
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Generate and save the city map
            city_map = folium.Map(location=[city.lat, city.lng], zoom_start=10)
            folium.Marker(location=[city.lat, city.lng], popup=city.city_name).add_to(city_map)
            city_map.save(f"{directory}/{city.city_name}_map.html")
            print("Map generated successfully.")
        else:
            print("City not found.")


    def sort_cities_by_population(self, order: str = 'A') -> list:
        """Sort cities by population."""
        if order.upper() == 'A':
            sorted_cities = sorted(self.cities_map, key=lambda x: x.population)
        elif order.upper() == 'D':
            sorted_cities = sorted(self.cities_map, key=lambda x: x.population, reverse=True)
        else:
            print("Invalid sorting order!")
            sorted_cities = []
        return sorted_cities


    
    def display_most_crowded_cities(self, n: int) -> None:
        """Display the most crowded cities."""
        sorted_cities = sorted(self.cities_map, key=lambda x: x.population, reverse=True)
        return sorted_cities[:n]
    
    def display_least_populated_city(self, n: int, order: str = 'A') -> list[City]:
        """Sort cities by population."""
        sorted_cities = sorted(self.cities_map, key=lambda x: x.population, reverse=(order.upper() == 'D'))
        return sorted_cities[:n]

    