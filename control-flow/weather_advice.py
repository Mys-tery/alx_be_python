#weather_advice.py

weather = input("Whats the weather like today? (sunny/rainy/cold): ")

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather =="rainy":
    print("Dont forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry,I dont have a recommendation for this weather.")