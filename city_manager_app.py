import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QInputDialog
from models.city import City
from main import cities_map

class CityManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('City Data Manager')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.city_name_input = QLineEdit()
        self.city_info_display = QTextEdit()
        self.city_operation_combo = QComboBox()
        self.submit_button = QPushButton('Submit')

        operations = [
            "Display City Information",
            "Display the Most Crowded N Cities",
            "Display the Least Populated N Cities",
            "Generate Entered City Map",
            "Display all Cities",
            "Sort Cities according to their Population",
            "Add Another City",
            "Exit"
        ]
        self.city_operation_combo.addItems(operations)

        self.submit_button.clicked.connect(self.handle_operation)

        layout.addWidget(QLabel('City Name:'))
        layout.addWidget(self.city_name_input)
        layout.addWidget(QLabel('Select Operation:'))
        layout.addWidget(self.city_operation_combo)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.city_info_display)

        self.setLayout(layout)

    def handle_operation(self):
        operation_index = self.city_operation_combo.currentIndex()
        self.city_info_display.clear()

        if operation_index == 0:  # Display City Information
            city_name = self.city_name_input.text()
            city = cities_map.display_city_info(city_name)
            if city:
                self.city_info_display.setText(
                    f"City Name: {city.city_name}\n"
                    f"Population: {city.population}\n"
                    f"Latitude: {city.lat}\n"
                    f"Longitude: {city.lng}"
                )
            else:
                self.city_info_display.setText("City not found.")

        elif operation_index == 1:  # Display the Most Crowded N Cities
            n, ok = QInputDialog.getInt(self, "Input", "Enter the number of cities:")
            if ok:
                most_crowded_cities = cities_map.display_most_crowded_cities(n)
                display_text = ""
                for city in most_crowded_cities:
                    display_text += f"City: {city.city_name}, Population: {city.population}\n"
                self.city_info_display.setText(display_text)

        elif operation_index == 2:  # Display the Least Populated N Cities
            n, ok = QInputDialog.getInt(self, "Input", "Enter the number of cities:")
            if ok:
                least_populated_cities = cities_map.display_least_populated_city(n, order='A')
                display_text = ""
                for city in least_populated_cities:
                    display_text += f"City: {city.city_name}, Population: {city.population}\n"
                self.city_info_display.setText(display_text)

        elif operation_index == 3:  # Generate Entered City Map
            city_name = self.city_name_input.text()
            cities_map.generate_city_map(city_name)
            self.city_info_display.setText("Map generated successfully.")

        elif operation_index == 4:  # Display all Cities
            all_cities_info = cities_map.display_all_cities()
            self.city_info_display.setText(all_cities_info)

        elif operation_index == 5:  # Sort Cities according to their Population
            order, ok = QInputDialog.getItem(self, "Select Order", "Sort cities in ascending (A) or descending (D) order:", ['A', 'D'], 0, False)
            if ok:
                sorted_cities = cities_map.sort_cities_by_population(order)
                display_text = ""
                for city in sorted_cities:
                    display_text += f"City: {city.city_name}, Population: {city.population}\n"
                self.city_info_display.setText(display_text)

        elif operation_index == 6:  # Add Another City
            city_name, ok1 = QInputDialog.getText(self, "Input", "Enter city name:")
            if ok1:
                lat, ok2 = QInputDialog.getDouble(self, "Input", "Enter latitude:")
                if ok2:
                    lng, ok3 = QInputDialog.getDouble(self, "Input", "Enter longitude:")
                    if ok3:
                        country, ok4 = QInputDialog.getText(self, "Input", "Enter country:")
                        if ok4:
                            population, ok5 = QInputDialog.getDouble(self, "Input", "Enter population:")
                            if ok5:
                                new_city = City(city_name, country, lng, lat, "", population)
                                cities_map.add_city(new_city)
                                self.city_info_display.setText("City added successfully!")

        elif operation_index == 7:  # Exit
            self.city_info_display.setText("Exiting the program...")
            QApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    city_manager_app = CityManagerApp()
    city_manager_app.show()
    sys.exit(app.exec_())
