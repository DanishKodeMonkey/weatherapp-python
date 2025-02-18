def get_weather_emoji(weather_id: int) -> str:
    """Return corresponding emoji to weather condition ID"""
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "☁️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 632:
        return "🌨️"
    elif 700 <= weather_id <= 741:
        return "🌫️"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "🌪️"
    elif weather_id == 800:
        return "🌞"
    elif 801 <= weather_id <= 804:
        return "☁️"
    else:
        return "?"
