# Python Weight Converter

weight = float(input("Enter the Weight: "))
unit = input("Kilos or Pounds? (K or L): ")

# kilo to pound conversion
if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your Weight is: {round(weight, 1)} {unit}")

# Pound to Kilo conversion
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your Weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} is not valid")

