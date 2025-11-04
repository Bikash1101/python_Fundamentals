weather = ["Sunny" , "Rainy" , "Snowy"]
weather_input = input("Enter The Weather: ")

if weather_input in weather:
    if weather_input == "Sunny":
        print("Go for a walk")
    elif weather_input == "Rainy":
        print("Read a book")
    elif weather_input == "Snowy":
        print("Build a Snowman")
else:
    print("Invaild weather input")