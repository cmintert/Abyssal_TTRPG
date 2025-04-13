from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple
import math
from ECS_Structure import Component


@dataclass
class MassComponent(Component):
    """Component for storing mass-related properties of celestial bodies."""
    mass_kg: float  # Mass in kilograms
    radius_km: float  # Radius in kilometers

    @property
    def density(self) -> float:
        """Calculate density in kg/m^3."""
        volume_m3 = (4 / 3) * math.pi * (self.radius_km * 1000) ** 3
        return self.mass_kg / volume_m3


@dataclass
class SystemPositionComponent(Component):
    """Component for storing position within a star system (in AU)."""
    x: float = 0.0  # x-coordinate in AU
    y: float = 0.0  # y-coordinate in AU
    z: float = 0.0  # z-coordinate in AU

    def distance_to(self, other: 'SystemPositionComponent') -> float:
        """Calculate distance to another position in AU."""
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)


class SpectralType(Enum):
    """Classification of stars based on their spectral characteristics."""
    O = "O"  # Blue, extremely hot and massive
    B = "B"  # Blue-white, very hot and massive
    A = "A"  # White, hot
    F = "F"  # Yellow-white, medium hot
    G = "G"  # Yellow, medium temperature (like our Sun)
    K = "K"  # Orange, cooler
    M = "M"  # Red, coolest main sequence stars
    L = "L"  # Brown dwarfs (not truly stars)
    T = "T"  # Methane dwarfs (not truly stars)
    Y = "Y"  # Coolest brown dwarfs
    WR = "WR"  # Wolf-Rayet star
    C = "C"  # Carbon star
    S = "S"  # Zirconium monoxide star


@dataclass
class StarComponent(Component):
    """Component for star-specific properties."""
    spectral_type: SpectralType  # Spectral classification
    surface_temperature_k: float  # Surface temperature in Kelvin
    luminosity_solar: float  # Luminosity relative to the Sun
    age_gyr: float  # Age in billions of years
    is_main_sequence: bool = True  # Whether the star is on the main sequence

    @property
    def habitable_zone(self) -> Tuple[float, float]:
        """
        Calculate the inner and outer bounds of the habitable zone in AU.
        Based on simple solar flux calculations.
        """
        # Simple approximation of habitable zone based on luminosity
        # Inner edge: where it's too hot for liquid water
        # Outer edge: where it's too cold for liquid water
        inner_edge = math.sqrt(self.luminosity_solar) * 0.75  # AU
        outer_edge = math.sqrt(self.luminosity_solar) * 1.8  # AU
        return inner_edge, outer_edge


@dataclass
class OrbitComponent(Component):
    """
    Component for orbital parameters using Keplerian elements.

    This allows for efficient calculation of positions over time without
    constantly running full n-body simulations.
    """
    # Primary orbital elements
    semi_major_axis: float  # Semi-major axis in AU
    eccentricity: float  # Orbital eccentricity (0 = circular, 1 = parabolic)
    inclination: float  # Orbital inclination in degrees
    longitude_of_ascending_node: float  # In degrees
    argument_of_periapsis: float  # In degrees
    mean_anomaly_at_epoch: float  # In degrees
    epoch: float  # Reference time for mean anomaly

    # Reference to the central body being orbited (star or planet ID)
    parent_id: str

    def calculate_position(self, time: float) -> Tuple[float, float, float]:
        """
        Calculate position using a parametric approximation that accounts for orbital shape
        and approximates speed variations.

        Args:
            time: Time since simulation start (in arbitrary time units)

        Returns:
            Tuple of (x, y, z) coordinates in AU
        """
        # Calculate orbital period using Kepler's third law
        # For this to be accurate, we assume time units where G*M_central = 1
        # For the Solar System with time in years, this works naturally
        period = 2 * math.pi * math.sqrt(self.semi_major_axis ** 3)

        # Calculate elapsed time since epoch
        elapsed_time = time - self.epoch

        # Calculate a parameter that increases linearly with time (0 to 2π over one period)
        # We use modulo to handle multiple orbits
        parameter = ((elapsed_time % period) / period) * 2 * math.pi

        # Add initial position offset from mean_anomaly_at_epoch
        parameter += math.radians(self.mean_anomaly_at_epoch)

        # Apply a simple correction to approximate speed variations
        # Objects move faster near periapsis (when parameter ≈ 0) and slower near apoapsis
        if self.eccentricity > 0.1:  # Only apply for noticeable eccentricities
            # This correction factor approximates some of the behavior of Kepler's equation
            # without requiring an iterative solution
            correction = 0.5 * self.eccentricity * math.sin(parameter)
            parameter += correction

        # Calculate semi-minor axis
        semi_minor_axis = self.semi_major_axis * math.sqrt(
            1 - self.eccentricity ** 2)

        # Calculate position in orbital plane using parametric form of ellipse
        # This places the central body at one focus of the ellipse
        x_orbital = self.semi_major_axis * math.cos(
            parameter) - self.eccentricity * self.semi_major_axis
        y_orbital = semi_minor_axis * math.sin(parameter)

        # Convert angles from degrees to radians for the rotation calculations
        incl = math.radians(self.inclination)
        node = math.radians(self.longitude_of_ascending_node)
        arg_peri = math.radians(self.argument_of_periapsis)

        # Perform the rotation transformations to convert from orbital plane to reference plane

        # First, rotate by argument of periapsis in orbital plane
        x_temp = x_orbital * math.cos(arg_peri) - y_orbital * math.sin(arg_peri)
        y_temp = x_orbital * math.sin(arg_peri) + y_orbital * math.cos(arg_peri)
        z_temp = 0

        # Then, rotate by inclination around the x-axis
        x_incl = x_temp
        y_incl = y_temp * math.cos(incl)
        z_incl = y_temp * math.sin(incl)

        # Finally, rotate by longitude of ascending node around the z-axis
        x = x_incl * math.cos(node) - y_incl * math.sin(node)
        y = x_incl * math.sin(node) + y_incl * math.cos(node)
        z = z_incl

        return (x, y, z)


@dataclass
class VisualComponent(Component):
    """Component for visual representation properties."""
    color: Tuple[int, int, int] = (255, 255, 255)  # RGB colour
    texture_name: Optional[str] = None  # Texture file reference
    display_size_factor: float = 1.0  # Factor to scale visual size (for display purposes)


@dataclass
class AtmosphereComponent(Component):
    """Component for atmospheric properties."""
    has_atmosphere: bool = False
    # Simple representation of the most abundant gases
    composition: List[Tuple[str, float]] = field(
        default_factory=list)  # List of (gas name, percentage)
    pressure_atm: float = 0.0  # Surface pressure in Earth atmospheres
    greenhouse_effect: float = 0.0  # Temperature increase due to greenhouse effect in Kelvin

    @property
    def is_breathable(self) -> bool:
        """
        Determine if the atmosphere is breathable by humans.
        Very simplified check for approximation.
        """
        if not self.has_atmosphere:
            return False

        oxygen_percent = 0.0
        nitrogen_percent = 0.0

        for gas, percentage in self.composition:
            if gas.lower() == "oxygen" or gas.lower() == "o2":
                oxygen_percent = percentage
            elif gas.lower() == "nitrogen" or gas.lower() == "n2":
                nitrogen_percent = percentage

        # Very simplified breathability check
        return (15 <= oxygen_percent <= 30 and
                nitrogen_percent >= 65 and
                0.5 <= self.pressure_atm <= 1.5)