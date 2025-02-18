from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt
from api import get_weather_data
from utils import get_weather_emoji


class WeatherApp(QWidget):
    # Constructor, initialize various UI elements
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    # UI  handles placement and customisation of elements
    def initUI(self):
        self.setWindowTitle("DKM WeatherApp")
        self.setFixedSize(400, 600)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet(
            """
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size:40px;
                font-style:italic;
                font-weight:bold;
            }
            QLineEdit#city_input{
                font-size:40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight:bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            
            }
            QLabel#emoji_label{
                font-size:100px;
                font-family: Segoe UI emoji;
            }

            QLabel#description_label{
                font-size:30px;
            }
        """
        )
        # connect clicked signal to get_weather
        self.get_weather_button.clicked.connect(self.get_weather)

    # API integration
    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            self.display_error("Please enter a city name.")
            return

        weather_data, error = get_weather_data(city)

        if error:
            self.display_error(error[0])  # Fail state, set error
        else:
            self.display_weather(weather_data)  # Success state, update UI

    # Error event
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    # Success event
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size:75px;")

        temperature_k = data["main"]["temp"]  # Kelvin temp
        temperature_c = temperature_k - 273.15  # Celcius temp
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:.2f}\N{DEGREE SIGN}C")
        self.emoji_label.setText(get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
