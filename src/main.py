import sys
from PyQt5.QtWidgets import QApplication
from ui import WeatherApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Weather_app = WeatherApp()
    Weather_app.show()
    sys.exit(app.exec_())  # Handle events in application, like closing the window.
