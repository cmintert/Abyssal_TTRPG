1. General Component Template

Prompt:

Please design a new component for [Component Type] in a space vessel. The component should [describe the function and
special features]. Include attributes such as [list any specific attributes like range, power consumption, etc.]. Format
the output as a Python dictionary with the fields data and type. Data contains the fields for Component Name, Type,
Component Size, Attribute 1, Attribute 2, Attribute 3, Attribute 4, Special Properties, EWDR, and Description.
Type contains the string value "component".

Use the following value ranges if applicable:

- Component Size: - Small Components (1 Slot): Basic Sensors, Small Utility Systems, Small Cargo
                  Hold (100 GST capacity), Basic Missile Magazine (1-2 small missiles or torpedoes, or a single medium
                  missile)

                  - Medium Components (2 Slots): Enhanced Sensors, Medium Utility Systems, Medium
                  Cargo Hold (200 GST capacity), Standard Missile Magazine (4-8 missiles or torpedoes)

                  - Large Components (3 Slots): Advanced Sensors, Large Utility Systems, Large Cargo
                  Hold (500 GST capacity), Heavy Missile Magazine (12-16 missiles, including long-range torpedos)

                  - Extra-Large Components (4+ Slots): Ship-Mounted Stellar Projector,
                  Extra-Large Cargo Hold (1000+ GST capacity), Strategic Missile Magazine (20+ missiles, including
                  torpedos and multi-warhead torpedos); Value is an integer

- Sensor Modifier: Negative (-3 to -1), Standard (0), Enhanced (+1 to +3), Advanced (+4 to +6)
- EWDR (Electronic Warfare Defense Rating): Low (+0), Moderate (+1), High (+2), Very High (+3)
- Description should be a string of text.

Values are either enclosed in quotes or not. Values cant have open quotes in them.

The dictionary is to be enclosed in {}, there is no variable name in front of it. Behind the last bracket is a colon.

Create proper indentation for the python dictionary.

2. General Ship Template

Prompt:

Please design a new ship for the game. The ship should be [describe the ship's role, size, and special features].
Include attributes such as acceleration, endurance, and armament. Format the output as a Python dictionary with the fields
data and type. Data contains the fields for Ship Name, Size (GST), Component Slots,Acceleration
(MaxG), Structural Endurance (StE), Electronic Endurance (ElE), Signal Rating (SiR), Armor, Cargo
Capacity (GST), Sensor Modifier, EWDR, Weapon Systems, Components, Crew Complement, and Description. Type contains
the string value "ship".

A ship has a KPAD (Kramer PAD Drive) for conventional propulsion.
It can be equipped with a Ship Mounted Stellar Projector, minimum Size of the ship is Medium.
Only if it has a Stellar Projector, it has to have an Instant Release High-Energy Capacitor (IRHEC)

Use the following value ranges:
- Name is a string and stands for a class of ships
- Size (GST): Small (200-800 GST), Medium (800-2000 GST), Large (2000-5000 GST), Very Large (5000+ GST), Capital (10,
  000+ GST); Value is an integer
- Component Slots: (GST/100 + 3); Value is an integer
- Acceleration (MaxG): Low (1), Moderate (1-3), High (3-6), Very High (6-9); Value is an integer
- Structural Endurance (StE): Low (1-5), Moderate (6-10), High (11-15), Very High (16-20); Value is an integer
- Electronic Endurance (ElE): Low (1-5), Moderate (6-10), High (11-15), Very High (16-20); Value is an integer
- Armor: Light (1-5), Moderate (6-10), Heavy (11-15), Very Heavy (16-20); Value is an integer
- Signal Rating (SiR): Low (1-5), Moderate (6-10), High (11-15), Very High (16-20); Value is an integer
- EWDR (Electronic Warfare Defense Rating): Low (0), Moderate (1-2), High (3-6), Very High (7-9); Value is an integer
- Weapon Systems; Value is a list of strings
- Components; Value is a list of strings
- Description should be a string of text. Included should be a rough size estimate in meters in 3 dimensions based upon
  the fact that a GST is roughly 3m^3.; Value is a string

Values are either enclosed in quotes or not. Values cant have open quotes in them.

The dictionary is to be enclosed in {}, there is no variable name in front of it. Behind the last bracket is a colon.

Create proper indentation for the python dictionary.

3. General Weapon Template

Prompt:

Please design a new weapon for a space vessel. The weapon should be [describe the type, range, and special abilities].
Include details like damage, penetration, and rate of fire. Format the output as a Python dictionary with the fields
data and type. Data contains the fields for Weapon Name, Type, Range Category, Damage, Penetration, EWAR, Rate of Fire,
Special Properties, Component Size, and Description. Type contains the string value "weapon".

Use the following value ranges:

- Damage: Low (1d6 to 2d6), Moderate (2d8 to 3d8), High (3d10 to 4d10), Very High (4d12 to 5d12+), Value is a string and
  enclosed in curly braces
- Penetration: Low (1-5), Moderate (6-10), High (11-15), Very High (16-20)
- EWAR (Electronic Warfare): Low (1-5), Moderate (6-10), High (11-15), Very High (16-20)
- Rate of Fire: Single, Burst, Sustained, Rapid Fire
- Component Size: Small Components (1 Slot): Light Weapon Systems
                  Medium Components (2 Slots): Medium Weapon Systems
                  Large Components (3 Slots): Heavy Weapon Systems
                  Extra-Large Components (4+ Slots): Capital-Class Weapon Systems ; Value is an integer

Values are either enclosed in quotes or not. Values cant have open quotes in them.

The dictionary is to be enclosed in {}, there is no variable name in front of it. Behind the last bracket is a colon.

Create proper indentation for the python dictionary.