import math

def convert_g_to_meters_per_second_squared(acceleration):
    return acceleration * 9.81

def calculate_travel_time(acceleration, initial_velocity, acceleration_time, range_category, continuous_acceleration):
    range_distances_km = {
        "Close Quarter": 1000,
        "Near": 10000,
        "Middle Range": 100000,
        "Long Range": 1000000,
        "Extreme Range": 10000000
    }

    acceleration_m_s2 = convert_g_to_meters_per_second_squared(acceleration)
    total_distance_m = range_distances_km.get(range_category, 0) * 1000  # Convert km to meters

    if continuous_acceleration:
        # Calculate time using kinematic equation for continuous acceleration
        total_time = (-initial_velocity + math.sqrt(initial_velocity**2 + 2 * acceleration_m_s2 * total_distance_m)) / acceleration_m_s2
    else:
        # Calculate distance covered during acceleration phase
        distance_acceleration = 0.5 * acceleration_m_s2 * (acceleration_time ** 2)

        # Final velocity after acceleration phase
        final_velocity = initial_velocity + acceleration_m_s2 * acceleration_time

        # Remaining distance to cover after acceleration phase
        remaining_distance = total_distance_m - distance_acceleration

        if remaining_distance > 0 and final_velocity > 0:
            # Time to cover remaining distance at constant velocity
            constant_velocity_time = remaining_distance / final_velocity
        else:
            constant_velocity_time = 0

        # Total travel time
        total_time = acceleration_time + constant_velocity_time

    return total_time

def get_user_input():
    while True:
        try:
            acceleration = float(input("Enter acceleration (G): "))
            initial_velocity = float(input("Enter initial velocity (m/s): "))
            acceleration_time = float(input("Enter acceleration time (s): "))
            continuous_acceleration = input("Continuous acceleration (yes/no): ").strip().lower() == 'yes'
            return acceleration, initial_velocity, acceleration_time, continuous_acceleration
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def display_table(acceleration, initial_velocity, acceleration_time, continuous_acceleration):
    print("\nTravel Time Calculation")
    print("-" * 50)
    print(f"{'Parameter':<25}{'Value':<25}")
    print("-" * 50)
    print(f"{'Acceleration (m/s^2)':<25}{convert_g_to_meters_per_second_squared(acceleration):<25}")
    print(f"{'Initial Velocity (m/s)':<25}{initial_velocity:<25}")
    print(f"{'Acceleration Time (s)':<25}{acceleration_time:<25}")
    print(f"{'Continuous Acceleration':<25}{continuous_acceleration:<25}")
    print("-" * 50)

    range_categories = ["Close Quarter", "Near", "Middle Range", "Long Range", "Extreme Range"]
    for category in range_categories:
        time_unit = "s"

        flight_time = calculate_travel_time(acceleration, initial_velocity, acceleration_time, category, continuous_acceleration)

        if flight_time > 60:
            flight_time /= 60
            time_unit = "min"
            if flight_time > 60:
                flight_time /= 60
                time_unit = "hr"
                if flight_time > 24:
                    flight_time /= 24
                    time_unit = "days"

        flight_time = round(flight_time, 2)

        print(f"{category:<25}{flight_time:<25} {time_unit}")
    print("-" * 50)

def main():
    while True:
        acceleration, initial_velocity, acceleration_time, continuous_acceleration = get_user_input()
        display_table(acceleration, initial_velocity, acceleration_time, continuous_acceleration)
        new_input = input("Do you want to make a new input? (yes/no): ").strip().lower()
        if new_input != 'yes':
            break

if __name__ == "__main__":
    main()
