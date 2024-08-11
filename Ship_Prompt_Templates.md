# Start of General Component Template Prompt ###

Please design a new component a space vessel in the Abyssal TTRPG game. The component should `[describe the function and special features]`.
Include attributes such as `[list any specific attributes like range, power consumption, etc.]`.
Please respect`[additional details]`

## Additional Details:

## Format the output as a Python dictionary with the following fields:

- **Data**: Contains the fields for Component Name, Type, Component Size, Attributes, Special Properties, EWDR, Rating, and Description.
- **Type**: Contains the string value `"component"`.

### Use the following value ranges if applicable:

#### Name [type: string]:
- The components name.
- The name includes a technical abbreviation with a shor version indicator.

#### Attributes [type: Dict of strings]
- Attribute names have to describe the value.
- Components can have multiple attributes.

#### Component Size [type: integer]:
- ** 1 (Small Components):**
  - Basic Sensors
  - Small Utility Systems
  - Small Cargo Hold (100 GST capacity)
  - Basic Missile Magazine (2 short range missiles or a single medium missile)

- ** 2 (Medium Components):**
  - Enhanced Sensors
  - Medium Utility Systems
  - Medium Cargo Hold (200 GST capacity)
  - Standard Missile Magazine (4-8 missiles)

- ** 3 (Large Components):**
  - Advanced Sensors
  - Large Utility Systems
  - Large Cargo Hold (500 GST capacity)
  - Heavy Missile Magazine (12-16 missiles, 2-6 long-range torpedoes)

- ** 4+ (Extra-Large Components):**
  - Ship-Mounted Stellar Projector
  - Extra-Large Cargo Hold (1000+ GST capacity)
  - Strategic Missile Magazine (20+ missiles, including torpedoes and multi-warhead torpedoes)

#### Sensor Modifier [type: integer]:
- **Negative**: (-3 to -1)
- **Standard**: (0)
- **Enhanced**: (+1 to +3)
- **Advanced**: (+4 to +6)

#### EWDR (Electronic Warfare Defense Rating) [type: integer]:
- **Low**: (+0)
- **Moderate**: (+1)
- **High**: (+2)
- **Very High**: (+3)

#### Rating [type: string]:
- Rate the component from 1 to 100.
- **Include an explanation of the rating** in 2 to 3 sentences. The explanation should cover:
    - The components usefulness relative to its size and type.
    - How the component fits into the overall balance of the game.
    - Considerations for the components intended role, special features, and potential gameplay impact.

### Description [type: string]:
- Should be a string of text.


### Python Dictionary Format:

- The dictionary should be enclosed in `{}`, with no variable name in front of it. After the last bracket there should be a comma `,`.
- Create proper indentation for the Python dictionary. 
- Values cannot have open quotes in them.
### Example Structure in Python:

{
    "data": {
        "Component Name": "Example Component Ex-2",
        "Type": "Component Type",
        "Component Size": 2,
        "Attributes": "Dict",
        "Special Properties": "Special Features",
        "EWDR": "Moderate",
        "Rating": "Is rated 20 because it is a medium-sized component with advanced sensors and utility systems.",
        "Description": "This is a detailed description of the component."
    },
    "type": "component"
},

### End of General Component Template Prompt ###

# Start of General Ship Template Prompt #

Please design a new ship for the in the Abyssal TTRPG game. The ship should be `[describe the ship's role, size, and 
special features]`. Include attributes such as acceleration, endurance, and armament.

## Additional Details:
- A ship has a **KPAD (Kramer PAD Drive)** for conventional propulsion.
- It can be equipped with a **Ship Mounted Stellar Projector**, with a minimum Size of the ship being Medium.
- Only if it has a Stellar Projector, it must have an **Instant Release High-Energy Capacitor (IRHEC)**.

## Format the output as a Python dictionary with the following fields:
- **Data**: Contains the fields for Ship Name, Size (GST), Component Slots, Acceleration (MaxG), Structural 
  Endurance (StE), Electronic Endurance (ElE), Signal Rating (SiR), Armor, Cargo Capacity (GST), Sensor Modifier, 
  EWDR, Weapon Systems, Components, Crew Complement, Rating, and Description.
- **Type**: Contains the string value `"ship"`.

### Use the following value ranges:

#### Name [type: string]:
- Stands for a class of ships.
- The name includes a technical abbreviation for the class.

#### Size (GST) [type: integer]:
- **Small**: (200-800 GST)
- **Medium**: (800-2000 GST)
- **Large**: (2000-5000 GST)
- **Very Large**: (5000+ GST)
- **Capital**: (10,000+ GST)

#### Component Slots [type: integer]:
- Formula: `(GST / 100) + 3`

#### Acceleration (MaxG) [type: integer]:
- **Low**: (1)
- **Moderate**: (1-3)
- **High**: (3-6)
- **Very High**: (6-9)

#### Structural Endurance (StE) [type: integer]:
- **Low**: (1-5)
- **Moderate**: (6-10)
- **High**: (11-15)
- **Very High**: (16-20)

#### Electronic Endurance (ElE) [type: integer]:
- **Low**: (1-5)
- **Moderate**: (6-10)
- **High**: (11-15)
- **Very High**: (16-20)

#### Armor [type: integer]:
- **Light**: (1-5)
- **Moderate**: (6-10)
- **Heavy**: (11-15)
- **Very Heavy**: (16-20)

#### Signal Rating (SiR) [type: integer]:
- **Low**: (1-5)
- **Moderate**: (6-10)
- **High**: (11-15)
- **Very High**: (16-20)

#### EWDR (Electronic Warfare Defense Rating) [type: integer]:
**Low**: (0)
**Moderate**: (1-2)
**High**: (3-6)
**Very High**: (7-9)

#### Weapon Systems [type: list of strings]:
- Value is a list of strings.

#### Components [type: list of strings]:
- Value is a list of strings.
- The added Component sizes can not be greater than the ship's Component Slots.

#### Rating [type: string]:
- Rate the ship from 1 to 100.
- **Include an explanation of the rating** in 2 to 3 sentences. The explanation should cover:
    - The Ships power relative to its size and type.
    - How the ship fits into the overall balance of the game.
    - Considerations for the ships's intended role, special features, and potential gameplay impact.


### Description [type: string]:
- Should be a string of text.
- Include a rough size estimate in meters in 3 dimensions, based on the fact that a GST is roughly 3m³.

### Python Dictionary Format:
-The dictionary should be enclosed in `{}`, with no variable name in front of it. 
-After the last bracket, there should be a colon `,`.
-Create proper indentation for the Python dictionary.

### Example Structure in Python:

{
    "data": {
        "Ship Name": "Example Class",
        "Size (GST)": 1500,
        "Component Slots": 18,
        "Acceleration (MaxG)": 4,
        "Structural Endurance (StE)": 12,
        "Electronic Endurance (ElE)": 10,
        "Signal Rating (SiR)": 8,
        "Armor": 14,
        "Cargo Capacity (GST)": 300,
        "Sensor Modifier": 2,
        "EWDR": 5,
        "Weapon Systems": ["Missile Launchers"],
        "Components": ["Kramer PAD Drive", "IRHEC", "Stellar Projector"],
        "Crew Complement": 150,
        "Rating": "Is rated 25 because it is a medium-sized ship with balanced stats and a good mix of weapons and components.",
        "Description": "A medium-sized vessel, approximately 50m x 30m x 20m, designed for long-range exploration and combat."
    },
    "type": "ship"
},

### End of General Ship Template Prompt ###

# Start General Weapon Template Prompt #

Please design a new weapon for a space vessel in the Abyssal TTRPG. The weapon should `[describe the type, range, and special abilities]`.

## Additional Details:
- Missile and torpedo weapons include the launchers as part of the weapon system. 
- Missile and torpedo magazines are separate Components and not weapons.
- Missile and torpedo launchers have a number of simultaneous loaded missiles or torpedoes, and a maxG Value as a special property.

## Format the output as a Python dictionary with the following fields:

- **Data**: Contains the fields for Weapon Name, Type, Range Category, Damage, Penetration, EWAR, Rate of Fire, 
  Special Properties, Component Size, Rating,and Description.
- **Type**: Contains the string value `"weapon"`.

### Use the following value ranges:

#### Name [type: string]:
- The weapon's name.
- The name includes a technical abbreviation based on weapon type.
- The name has to sound martial.

#### Type [type: string]
- Short Range Missile
- Long Range Missile
- Torpedo
- Point Defence Gauss Weapon
- Large Calibre Gauss Cannon
- Conventional Projectile Weapon (CPW). CPW use a propellant to fire a solid projectile. 

#### Range Category [type: string]:
- Close Quarter ( < 1000 km ) 
- Near ( 1000 km - 10000 km )
- Middle Range ( 10000 km - 100000 km )
- Long Range ( 100000 km - 1000000 km )
- Extreme Range ( > 1000000 km )

#### Damage [type: string]:
- **Low**: (`"1d6"` to `"2d6"`)
- **Moderate**: (`"2d8"` to `"3d8"`)
- **High**: (`"3d10"` to `"4d10"`)
- **Very High**: (`"4d12"` to `"5d12+"`)

#### Penetration [type: integer]:
- **Low**: (1-5)
- **Moderate**: (6-10)
- **High**: (11-15)
- **Very High**: (16-20)

#### EWAR (Electronic Warfare) [type: integer]:
- **Low**: (1-5)
- **Moderate**: (6-10)
- **High**: (11-15)
- **Very High**: (16-20)

#### Rate of Fire [type: string]:
- **Options**: `"Single"`, `"Burst"`, `"Sustained"`, `"Rapid Fire"`

#### Component Size [type: integer]:
- **Small Components (1 Slot)**:
  -Light Weapon Systems
- **Medium Components (2 Slots)**: 
  -Medium Weapon Systems
- **Large Components (3 Slots)**: 
  -Heavy Weapon Systems
- **Extra-Large Components (4+ Slots)**: 
  -Capital-Class Weapon Systems
  
#### Rating [type: string]:
- Rate the weapon from 1 to 100.
- **Include an explanation of the rating** in 2 to 3 sentences. The explanation should cover:
    - The weapon's power relative to its size and type.
    - How the weapon fits into the overall balance of the game.
    - Considerations for the weapon's intended role, special features, and potential gameplay impact.

- 
#### Description [type: string]:
- Should be a string of text.

### Python Dictionary Format:
- The dictionary should be enclosed in `{}`, with no variable name in front of it.
- After the last bracket, there should be a colon `,`.
- Create proper indentation for the Python dictionary.

### Example Structure in Python:

{
    "data": {
        "Weapon Name": "Example Weapon",
        "Type": "Weapon Type",
        "Range Category": "Long Range",
        "Damage": "4d10",
        "Penetration": 12,
        "EWAR": 8,
        "Rate of Fire": "Sustained",
        "Special Properties": "Armor-piercing, EMP-capable",
        "Component Size": 3,
        "Rating": "It is rated 15 because it is a heavy weapon system with high penetration and EMP capabilities.",
        "Description": "A powerful heavy weapon system designed for long-range engagements, featuring high penetration and EMP capabilities."
    },
    "type": "weapon"
},

### End General Weapon Template Prompt ###