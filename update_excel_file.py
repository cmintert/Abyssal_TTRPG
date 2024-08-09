import pandas as pd

# Load the data
excel_file = 'Abyssal_Ship_Hardware.xlsx'
weapons = pd.read_excel(excel_file, sheet_name='Weapons')
ships = pd.read_excel(excel_file, sheet_name='Ships')
components = pd.read_excel(excel_file, sheet_name='Components')

# Function to handle updates based on type
def update_excel(data, data_type):
    if data_type == 'weapon':
        global weapons
        new_data_df = pd.DataFrame([data])
        weapons = pd.concat([weapons, new_data_df], ignore_index=True)
    elif data_type == 'ship':
        global ships
        new_data_df = pd.DataFrame([data])
        ships = pd.concat([ships, new_data_df], ignore_index=True)
    elif data_type == 'component':
        global components
        new_data_df = pd.DataFrame([data])
        components = pd.concat([components, new_data_df], ignore_index=True)
    else:
        print(f"Unknown data type: {data_type}")

# Example bulk updates
bulk_updates = [
    {
        "data": {
            "Ship Name": "Falcon Scout",
            "Size (GST)": 300,
            "Acceleration (Cruise/March/Max in Gs)": "3G/6G/12G",
            "Structural Endurance (StE)": 8,
            "Electronic Endurance (ElE)": 10,
            "Signal Rating (SiR)": 6,
            "Armor": 4,
            "Cargo Capacity (GST)": 50,
            "Sensor Modifier": "+3",
            "EWDR": "+2",
            "Weapon Systems": "Dual Light Pulse Lasers",
            "Special Systems": "Stealth Suite, Advanced Sensor Package",
            "Crew Complement": "3 (Pilot, Sensor Operator, Engineer)",
            "Description": "The Falcon Scout is a nimble reconnaissance craft designed for rapid deployment and stealth operations. Equipped with advanced sensors and light armament, it excels in gathering intelligence and avoiding detection."
        },
        "type": "ship"
    },

    {
        "data": {
            "Ship Name": "Hawk-Eye Recon",
            "Size (GST)": 280,
            "Acceleration (Cruise/March/Max in Gs)": "3G/5G/10G",
            "Structural Endurance (StE)": 7,
            "Electronic Endurance (ElE)": 11,
            "Signal Rating (SiR)": 5,
            "Armor": 3,
            "Cargo Capacity (GST)": 40,
            "Sensor Modifier": "+4",
            "EWDR": "+1",
            "Weapon Systems": "Single Gauss Cannon",
            "Special Systems": "Long-Range Scanners, Electronic Countermeasures",
            "Crew Complement": "2 (Pilot, Sensor Operator)",
            "Description": "The Hawk-Eye Recon is a small, agile scout ship equipped with long-range sensors and minimal armament. Its primary role is to gather intelligence and provide early warning of enemy activity."
        },
        "type": "ship"
    },
    {
        "data": {
            "Ship Name": "Wasp Interceptor",
            "Size (GST)": 350,
            "Acceleration (Cruise/March/Max in Gs)": "4G/7G/14G",
            "Structural Endurance (StE)": 9,
            "Electronic Endurance (ElE)": 9,
            "Signal Rating (SiR)": 7,
            "Armor": 5,
            "Cargo Capacity (GST)": 60,
            "Sensor Modifier": "+2",
            "EWDR": "+2",
            "Weapon Systems": "Light Missile Pod, Twin Plasma Cannons",
            "Special Systems": "Enhanced Thrusters, Advanced Targeting System",
            "Crew Complement": "3 (Pilot, Weapons Officer, Engineer)",
            "Description": "The Wasp Interceptor is a versatile scout craft designed for both reconnaissance and light combat. With its fast acceleration and light weaponry, it can quickly engage and disengage from hostile situations."
        },
        "type": "ship"
    }
]
# Process each update
for update in bulk_updates:
    update_excel(update['data'], update['type'])

# Save the updated data back to the Excel file
with pd.ExcelWriter(excel_file) as writer:
    weapons.to_excel(writer, sheet_name='Weapons', index=False)
    ships.to_excel(writer, sheet_name='Ships', index=False)
    components.to_excel(writer, sheet_name='Components', index=False)

print("Bulk updates completed and saved to the Excel file.")
