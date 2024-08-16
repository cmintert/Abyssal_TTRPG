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

def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_user_input():
    ACCELERATION_PROMPT = "Enter acceleration (G): "
    INITIAL_VELOCITY_PROMPT = "Enter initial velocity (m/s): "
    ACCELERATION_TIME_PROMPT = "Enter acceleration time (s): "
    CONTINUOUS_ACCELERATION_PROMPT = "Continuous acceleration (yes/no): "

    acceleration = get_float_input(ACCELERATION_PROMPT)
    initial_velocity = get_float_input(INITIAL_VELOCITY_PROMPT)
    acceleration_time = get_float_input(ACCELERATION_TIME_PROMPT)

    while True:
        continuous_acceleration_input = input(CONTINUOUS_ACCELERATION_PROMPT).strip().lower()
        if continuous_acceleration_input in ['yes', 'no']:
            continuous_acceleration = (continuous_acceleration_input == 'yes')
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return acceleration, initial_velocity, acceleration_time, continuous_acceleration


def convert_and_format_flight_time(flight_time):
    time_units = [("s", 60), ("min", 60), ("hr", 24), ("days", None)]
    for unit, divisor in time_units:
        if divisor is None or flight_time <= divisor:
            return round(flight_time, 2), unit
        flight_time /= divisor

def display_table(acceleration, initial_velocity, acceleration_time, continuous_acceleration):

    print("\nTravel Time Calculation")
    print("-" * 50)
    print(f"{'Parameter':<25}{'Value':<25}")
    print("-" * 50)
    print(f"{'Acceleration (G)':<25}{acceleration:<10}")
    print(f"{'Initial Velocity (m/s)':<25}{initial_velocity:<10}")
    print(f"{'Acceleration Time (s)':<25}{acceleration_time:<10}")
    print(f"{'Continuous Acceleration':<25}{continuous_acceleration:<10}")
    print("-" * 50)

    range_categories = ["Close Quarter", "Near", "Middle Range", "Long Range", "Extreme Range"]
    for category in range_categories:
        flight_time = calculate_travel_time(acceleration, initial_velocity, acceleration_time, category,
                                            continuous_acceleration)
        flight_time, time_unit = convert_and_format_flight_time(flight_time)
        print(f"{category:<25}{flight_time:<10} {time_unit}")
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
