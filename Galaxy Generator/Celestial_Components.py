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
        Calculate the position in the orbital plane at a given time.

        This is a simplified implementation. A real one would solve Kepler's equation
        and perform the necessary coordinate transformations.

        Args:
            time: Time since epoch

        Returns:
            Tuple of (x, y, z) coordinates in AU
        """
        # This would normally implement Kepler's equation solution
        # For now, we'll return a simple circular approximation

        # Mean motion (radians per time unit)
        mean_motion = 2 * math.pi / (self.semi_major_axis ** 1.5)

        # Current angle in orbit
        angle = math.radians(self.mean_anomaly_at_epoch) + mean_motion * (
                    time - self.epoch)

        # Simple circular approximation
        x = self.semi_major_axis * math.cos(angle)
        y = self.semi_major_axis * math.sin(angle) * math.cos(
            math.radians(self.inclination))
        z = self.semi_major_axis * math.sin(angle) * math.sin(
            math.radians(self.inclination))

        return x, y, z


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