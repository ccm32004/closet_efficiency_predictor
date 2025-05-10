import pandas as pd
import os

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Options for each category
BRANDS = ["Aritzia", "Garage", "Dynamite", "Lululemon", "Shein", "H&M", "American Eagle", "Ardene", "Hollister", "Tankair", "Other"]
TYPES = ["athleisure", "coquette", "casual", "workwear", "eveningwear", "basics", "party"]
FITS = ["tight", "oversized", "structured", "flowy"]
COLORS = ["neutrals", "pastels", "bold", "earth tones", "black/white", "patterned"]

# Data storage
data = {
    "brand": [],
    "type": [],
    "fit": [],
    "color": [],
    "trendy": [],
    "comfort_level": [],
    "revealing_level": [],
    "fabric_quality": [],
    "wear_frequency": []
}

def choose_option(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"{i}: {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 0 <= choice < len(options):
                return options[choice]
            else:
                print(" Invalid choice. Try again.")
        except ValueError:
            print(" Please enter a number.")

def collect_item():
    brand = choose_option("Select brand:", BRANDS)
    type_ = choose_option("Select type of clothing:", TYPES)
    fit = choose_option("Select fit:", FITS)
    color = choose_option("Select color palette:", COLORS)
    trendy = input("\nIs this item trendy right now? (y/n): ").strip().lower()
    trendy_bool = 1 if trendy == 'y' else 0
    comfort = int(input("\nComfort level (1 = bad, 5 = super comfy): "))
    
    revealing = int(input("\nRevealing level? (1 = not revealing, 2 = medium, 3 = very revealing): "))
    while revealing not in [1, 2, 3]:
        print("Please enter 1, 2, or 3.")
        revealing = int(input("Revealing level? (1 = not revealing, 2 = medium, 3 = very revealing): "))

    fabric_quality = int(input("\nFabric quality rating? (1 = bad quality, 5 = luxury quality): "))
    while fabric_quality not in [1, 2, 3, 4, 5]:
        print("Please enter a number between 1 and 5.")
        fabric_quality = int(input("Fabric quality rating? (1 = bad quality, 5 = luxury quality): "))

    wear_percent = int(input("\nHow often do you think you'll wear this in the next 3 months? (0–100%): "))
    wear_freq = wear_percent / 100.0

    data["brand"].append(brand)
    data["type"].append(type_)
    data["fit"].append(fit)
    data["color"].append(color)
    data["trendy"].append(trendy_bool)
    data["comfort_level"].append(comfort)
    data["revealing_level"].append(revealing)
    data["fabric_quality"].append(fabric_quality)
    data["wear_frequency"].append(wear_freq)

# Main loop
print("👗 Welcome to the Closet Data Collector!")
while True:
    collect_item()
    cont = input("\nAdd another item? (y/n): ").strip().lower()
    if cont != 'y':
        break

# Check if the CSV file already exists
csv_path = "data/closet_items.csv"

if os.path.exists(csv_path):
    # If file exists, load it and append new data
    old_df = pd.read_csv(csv_path)
    new_df = pd.DataFrame(data)
    df = pd.concat([old_df, new_df], ignore_index=True)
else:
    # If file doesn't exist yet, create new DataFrame
    df = pd.DataFrame(data)

# Save to CSV
df.to_csv(csv_path, index=False)
print("\nData saved to 'data/closet_items.csv'!")
