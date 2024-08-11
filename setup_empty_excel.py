import pandas as pd

# Define the structure for each sheet (Weapons, Ships, Components)
# These are empty dictionaries to represent the initial structure.

# Weapon Data Structure
weapon_data = {
    "Weapon Name": [],
    "Type": [],
    "Range Category": [],
    "Damage": [],
    "Penetration": [],
    "EWAR": [],
    "Rate of Fire": [],
    "Special Properties": [],
    "Component Size": [],
    "Rating": [],
    "Description": []
}

# Ship Data Structure
ship_data = {
    "Ship Name": [],
    "Size (GST)": [],
    "Component Slots": [],
    "Acceleration (MaxG)": [],
    "Structural Endurance (StE)": [],
    "Electronic Endurance (ElE)": [],
    "Signal Rating (SiR)": [],
    "Armor": [],
    "Cargo Capacity (GST)": [],
    "Sensor Modifier": [],
    "EWDR": [],
    "Weapon Systems": [],
    "Components": [],
    "Crew Complement": [],
    "Rating": [],
    "Description": []
}

# Component Data Structure
component_data = {
    "Component Name": [],
    "Type": [],
    "Component Size": [],
    "Special Properties": [],
    "EWDR": [],
    "Rating": [],
    "Description": []
}

# Convert dictionaries to DataFrames
weapon_df = pd.DataFrame(weapon_data)
ship_df = pd.DataFrame(ship_data)
component_df = pd.DataFrame(component_data)

# Create an Excel writer object and write the DataFrames to different sheets
excel_filename = 'Abyssal_Ship_Hardware.xlsx'

with pd.ExcelWriter(excel_filename) as writer:
    weapon_df.to_excel(writer, sheet_name='Weapons', index=False)
    ship_df.to_excel(writer, sheet_name='Ships', index=False)
    component_df.to_excel(writer, sheet_name='Components', index=False)

print(f"Empty Excel file '{excel_filename}' created successfully.")