# def forecast(*data):
    # weather_main = {
    #     "Sunny": [],
    #     "Cloudy": [],
    #     "Rainy": []
    # }
    # for location, weather in data:
    #     if weather == "Sunny":
    #         weather_main[weather].append(location)
    #     elif weather == "Cloudy":
    #         weather_main[weather].append(location)
    #     elif weather == "Rainy":
    #         weather_main[weather].append(location)
    #
    # output = ""
    #
    # for key, value in weather_main.items():
    #     sorted_elements = sorted(value, key=lambda x: x)
    #     for element in sorted_elements:
    #         output += f"{element} - {key}\n"
    # return output

def forecast(*data):
    result = []

    def add_locations(type_of_locations):
        locations = []

        for location, weather in data:
            if weather == type_of_locations:
                locations.append(location)

        for l in sorted(locations):
            result.append(f"{l} - {type_of_locations}")

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")

    return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
