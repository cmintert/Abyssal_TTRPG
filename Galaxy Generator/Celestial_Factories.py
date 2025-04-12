import random
import math
from typing import Optional, Tuple, List
from ECS_Structure import World, Entity
from Celestial_Components import (
    MassComponent,
    SystemPositionComponent,
    StarComponent,
    OrbitComponent,
    VisualComponent,
    AtmosphereComponent,
    SpectralType
)


class StarFactory:
    """
    Factory for creating star entities with realistic properties.
    This class provides static methods for generating star entities based on their
    spectral classification and other parameters. Generated entities are equipped with
    appropriate components such as mass, position, stellar properties, and visual attributes.

    Attributes:
        None, as all methods are static.
    """

    @staticmethod
    def create_star(world: World,
                    spectral_type: SpectralType,
                    position: Tuple[float, float, float] = (0, 0, 0),
                    custom_mass: Optional[float] = None,
                    custom_radius: Optional[float] = None,
                    custom_temp: Optional[float] = None,
                    custom_luminosity: Optional[float] = None,
                    custom_age: Optional[float] = None) -> Entity:
        """
        Create a star with properties based on its spectral type.

        Args:
            world: The ECS world to add the star to
            spectral_type: Spectral classification of the star
            position: (x, y, z) position in AU
            custom_*: Optional override values for star properties

        Returns:
            The created star entity
        """
        # Create a new entity
        star_entity = world.create_entity()

        # Set default properties based on spectral type
        mass_solar, radius_solar, temp_k, luminosity_solar, color = \
            StarFactory._get_properties_for_spectral_type(spectral_type)

        # Override with custom values if provided
        if custom_mass is not None:
            mass_solar = custom_mass
        if custom_radius is not None:
            radius_solar = custom_radius
        if custom_temp is not None:
            temp_k = custom_temp
        if custom_luminosity is not None:
            luminosity_solar = custom_luminosity

        # Convert solar mass to kg
        mass_kg = mass_solar * 1.989e30  # Solar mass in kg

        # Convert solar radius to km
        radius_km = radius_solar * 695700  # Solar radius in km

        # Set random age if not specified
        if custom_age is None:
            # Stars can live up to about 10 billion years for G-type
            # Adjust lifespan based on mass (more massive stars live shorter lives)
            max_age = 10.0 * (1.0 / mass_solar)  # Rough approximation
            age_gyr = random.uniform(0.1,
                                     max_age * 0.8)  # Avoid stars at end of life
        else:
            age_gyr = custom_age

        # Add components
        star_entity.add_component(
            MassComponent(mass_kg=mass_kg, radius_km=radius_km))
        star_entity.add_component(
            SystemPositionComponent(x=position[0], y=position[1],
                                    z=position[2]))
        star_entity.add_component(StarComponent(
            spectral_type=spectral_type,
            surface_temperature_k=temp_k,
            luminosity_solar=luminosity_solar,
            age_gyr=age_gyr
        ))
        star_entity.add_component(VisualComponent(color=color))

        return star_entity

    @staticmethod
    def _get_properties_for_spectral_type(spectral_type: SpectralType) -> Tuple[
        float, float, float, float, Tuple[int, int, int]]:
        """
        Get realistic properties for a given spectral type.

        Returns:
            Tuple of (mass_solar, radius_solar, temp_k, luminosity_solar, color_rgb)
        """
        # These are approximate values for main sequence stars
        properties = {
            SpectralType.O: (20.0, 10.0, 30000, 100000.0, (155, 176, 255)),
            # Blue
            SpectralType.B: (7.0, 4.0, 15000, 1000.0, (170, 191, 255)),
            # Blue-white
            SpectralType.A: (2.0, 1.7, 9000, 20.0, (202, 215, 255)),  # White
            SpectralType.F: (1.3, 1.2, 7000, 3.0, (248, 247, 255)),
            # Yellow-white
            SpectralType.G: (1.0, 1.0, 5700, 1.0, (255, 244, 232)),
            # Yellow (Sun-like)
            SpectralType.K: (0.8, 0.8, 4500, 0.3, (255, 210, 161)),  # Orange
            SpectralType.M: (0.3, 0.4, 3000, 0.03, (255, 204, 111)),  # Red
            # Add properties for other spectral types as needed
        }

        # Default to G-type if spectral type not found
        return properties.get(spectral_type, properties[SpectralType.G])


class PlanetFactory:
    """Factory for creating planet entities with realistic properties."""

    @staticmethod
    def create_planet(world: World,
                      parent_star: Entity,
                      distance_from_star: float,
                      planet_type: str,
                      custom_mass: Optional[float] = None,
                      custom_radius: Optional[float] = None,
                      custom_eccentricity: Optional[float] = None,
                      custom_inclination: Optional[float] = None) -> Entity:
        """
        Create a planet with properties based on its type.

        Args:
            world: The ECS world to add the planet to
            parent_star: The star this planet orbits
            distance_from_star: Orbital distance in AU
            planet_type: Type of planet (e.g., "rocky", "gas_giant", "ice_giant")
            custom_*: Optional override values for planet properties

        Returns:
            The created planet entity
        """
        # Create a new entity
        planet_entity = world.create_entity()

        # Get default planet properties based on type
        mass_earth, radius_earth, has_atmosphere, color = \
            PlanetFactory._get_properties_for_planet_type(planet_type)

        # Override with custom values if provided
        if custom_mass is not None:
            mass_earth = custom_mass
        if custom_radius is not None:
            radius_earth = custom_radius

        # Set orbital parameters
        if custom_eccentricity is None:
            eccentricity = random.uniform(0.0,
                                          0.1)  # Most stable planets have low eccentricity
        else:
            eccentricity = custom_eccentricity

        if custom_inclination is None:
            inclination = random.uniform(0.0,
                                         10.0)  # Most solar system planets have low inclination
        else:
            inclination = custom_inclination

        # Random orbital angle parameters
        longitude_node = random.uniform(0.0, 360.0)
        argument_periapsis = random.uniform(0.0, 360.0)
        mean_anomaly = random.uniform(0.0, 360.0)

        # Convert Earth mass to kg
        mass_kg = mass_earth * 5.972e24  # Earth mass in kg

        # Convert Earth radius to km
        radius_km = radius_earth * 6371  # Earth radius in km

        # Add components
        planet_entity.add_component(
            MassComponent(mass_kg=mass_kg, radius_km=radius_km))

        # Initial position is calculated from orbital parameters
        planet_entity.add_component(SystemPositionComponent(x=0, y=0, z=0))

        # Add orbital component
        planet_entity.add_component(OrbitComponent(
            semi_major_axis=distance_from_star,
            eccentricity=eccentricity,
            inclination=inclination,
            longitude_of_ascending_node=longitude_node,
            argument_of_periapsis=argument_periapsis,
            mean_anomaly_at_epoch=mean_anomaly,
            epoch=0.0,  # Current simulation time
            parent_id=parent_star.id
        ))

        planet_entity.add_component(VisualComponent(color=color))

        # Add atmosphere component if applicable
        if has_atmosphere:
            # Different planet types would have different atmospheres
            if planet_type == "rocky":
                # Earth-like
                composition = [("Nitrogen", 78.0), ("Oxygen", 21.0),
                               ("Argon", 0.9), ("Carbon Dioxide", 0.1)]
                pressure = random.uniform(0.5, 1.5)  # Earth = 1
                greenhouse = random.uniform(10, 40)  # Earth ~ 33K
            elif planet_type == "gas_giant":
                # Jupiter-like
                composition = [("Hydrogen", 90.0), ("Helium", 10.0)]
                pressure = random.uniform(100, 1000)
                greenhouse = 0.0  # Not relevant for gas giants
            else:
                # Generic atmosphere
                composition = [("Unknown", 100.0)]
                pressure = random.uniform(0.1, 10.0)
                greenhouse = random.uniform(0, 100)

            planet_entity.add_component(AtmosphereComponent(
                has_atmosphere=True,
                composition=composition,
                pressure_atm=pressure,
                greenhouse_effect=greenhouse
            ))

        return planet_entity

    @staticmethod
    def _get_properties_for_planet_type(planet_type: str) -> Tuple[
        float, float, bool, Tuple[int, int, int]]:
        """
        Get realistic properties for a given planet type.

        Returns:
            Tuple of (mass_earth, radius_earth, has_atmosphere, color_rgb)
        """
        # These are approximate values for different planet types
        properties = {
            "rocky": (1.0, 1.0, True, (100, 149, 237)),  # Blue/Earth-like
            "rocky_small": (0.4, 0.6, False, (188, 143, 143)),
            # Brown/Mars-like
            "rocky_large": (2.0, 1.4, True, (144, 238, 144)),
            # Light green/Super-Earth
            "gas_giant": (300.0, 11.0, True, (255, 222, 173)),
            # Beige/Jupiter-like
            "ice_giant": (14.0, 4.0, True, (173, 216, 230)),
            # Light blue/Neptune-like
            "ocean_world": (1.2, 1.1, True, (0, 105, 148)),  # Deep blue
            "desert_world": (0.8, 0.9, True, (210, 180, 140)),  # Tan
            "lava_world": (0.9, 0.9, True, (255, 69, 0)),  # Red-orange
        }

        # Default to rocky if type not found
        return properties.get(planet_type, properties["rocky"])


class MoonFactory:
    """Factory for creating moon entities orbiting planets."""

    @staticmethod
    def create_moon(world: World,
                    parent_planet: Entity,
                    distance_from_planet: float,  # in planet radii
                    moon_type: str = "rocky_small",
                    custom_mass: Optional[float] = None,
                    custom_radius: Optional[float] = None) -> Entity:
        """
        Create a moon orbiting a planet.

        Args:
            world: The ECS world to add the moon to
            parent_planet: The planet this moon orbits
            distance_from_planet: Orbital distance in planet radii
            moon_type: Type of moon (e.g., "rocky_small", "icy")
            custom_*: Optional override values for moon properties

        Returns:
            The created moon entity
        """
        # Similar implementation to PlanetFactory but with adjustments for moons
        # Would calculate position relative to the parent planet
        # For brevity, implementation details are omitted

        # Create a basic moon
        moon_entity = world.create_entity()

        # Calculate mass and radius - moons are generally smaller than planets
        if moon_type == "rocky_small":
            # Earth's Moon-like
            mass_earth = 0.01 if custom_mass is None else custom_mass
            radius_earth = 0.27 if custom_radius is None else custom_radius
            color = (200, 200, 200)  # Gray
        elif moon_type == "icy":
            # Europa-like
            mass_earth = 0.008 if custom_mass is None else custom_mass
            radius_earth = 0.25 if custom_radius is None else custom_radius
            color = (220, 220, 240)  # Bluish-white
        else:
            # Generic small moon
            mass_earth = 0.005 if custom_mass is None else custom_mass
            radius_earth = 0.2 if custom_radius is None else custom_radius
            color = (180, 180, 180)  # Light gray

        # Convert to kg and km
        mass_kg = mass_earth * 5.972e24
        radius_km = radius_earth * 6371

        # Get parent planet properties
        planet_mass = parent_planet.get_component(MassComponent)

        # Calculate orbital period using Kepler's laws (approximation)
        # Convert planet radii to AU for consistency
        planet_radius_au = planet_mass.radius_km / 149597870.7  # km to AU
        distance_au = distance_from_planet * planet_radius_au

        # Add components
        moon_entity.add_component(
            MassComponent(mass_kg=mass_kg, radius_km=radius_km))
        moon_entity.add_component(SystemPositionComponent(x=0, y=0, z=0))
        moon_entity.add_component(OrbitComponent(
            semi_major_axis=distance_au,
            eccentricity=random.uniform(0.0, 0.05),
            inclination=random.uniform(0.0, 5.0),
            longitude_of_ascending_node=random.uniform(0.0, 360.0),
            argument_of_periapsis=random.uniform(0.0, 360.0),
            mean_anomaly_at_epoch=random.uniform(0.0, 360.0),
            epoch=0.0,
            parent_id=parent_planet.id
        ))
        moon_entity.add_component(VisualComponent(color=color))

        return moon_entity


class StarSystemFactory:
    """Factory for creating complete star systems."""

    @staticmethod
    def create_system(world: World,
                      star_type: SpectralType = SpectralType.G,
                      num_planets: Optional[int] = None,
                      include_moons: bool = True) -> List[Entity]:
        """
        Create a complete star system with a primary star and planets.

        Args:
            world: The ECS world to add the system to
            star_type: Spectral type of the primary star
            num_planets: Number of planets to generate (if None, will generate a random number)
            include_moons: Whether to include moons around suitable planets

        Returns:
            List of all entities in the created system
        """
        system_entities = []

        # Create the primary star
        primary_star = StarFactory.create_star(world, star_type)
        system_entities.append(primary_star)

        # Get star properties to inform planet generation
        star_component = primary_star.get_component(StarComponent)
        inner_hz, outer_hz = star_component.habitable_zone

        # Determine number of planets if not specified
        if num_planets is None:
            num_planets = random.randint(1, 8)  # Random number of planets

        # Calculate plausible orbital distances
        # Simple model: each orbit increases by a factor using the Titius-Bode rule
        orbital_distances = []
        for i in range(num_planets):
            if i == 0:
                # First planet - random close distance
                distance = random.uniform(0.1, 0.4)
            else:
                # Subsequent planets - roughly follow Titius-Bode
                prev_distance = orbital_distances[-1]
                min_spacing = prev_distance * 0.4  # Minimum spacing factor
                max_spacing = prev_distance * 0.8  # Maximum spacing factor

                # Add some randomness but ensure increasing distance
                distance = prev_distance + random.uniform(min_spacing,
                                                          max_spacing)

            orbital_distances.append(distance)

        # Create planets
        for i, distance in enumerate(orbital_distances):
            # Determine planet type based on distance from star and habitability zone
            if distance < inner_hz * 0.5:
                # Inner system - rocky or lava
                if distance < inner_hz * 0.3:
                    planet_type = "lava_world"
                else:
                    planet_type = "rocky" if random.random() < 0.7 else "desert_world"
            elif inner_hz <= distance <= outer_hz:
                # Habitable zone - mostly rocky/Earth-like
                planet_type = "rocky" if random.random() < 0.8 else "ocean_world"
            elif distance < outer_hz * 2.0:
                # Outer habitable - mix of rocky and ice
                planet_type = "rocky_large" if random.random() < 0.4 else "ice_giant"
            else:
                # Outer system - gas and ice giants
                planet_type = "gas_giant" if random.random() < 0.6 else "ice_giant"

            # Create the planet
            planet = PlanetFactory.create_planet(
                world, primary_star, distance, planet_type
            )
            system_entities.append(planet)

            # Add moons to some planets
            if include_moons and planet_type in ["rocky", "rocky_large",
                                                 "gas_giant", "ice_giant"]:
                # More moons for bigger planets
                max_moons = 1 if planet_type == "rocky" else 5
                num_moons = random.randint(0, max_moons)

                for m in range(num_moons):
                    # Moons orbit at 3-30 planet radii
                    moon_distance = random.uniform(3.0, 30.0)
                    moon_type = "icy" if random.random() < 0.5 else "rocky_small"

                    moon = MoonFactory.create_moon(
                        world, planet, moon_distance, moon_type
                    )
                    system_entities.append(moon)

        return system_entities


# Example usage
def example_create_solar_system():
    """Create an example star system similar to our solar system."""
    world = World()

    # Create a solar system with a G-type star (like our Sun)
    solar_system = StarSystemFactory.create_system(
        world,
        star_type=SpectralType.G,
        num_planets=8,  # Like our solar system
        include_moons=True
    )

    # For demonstration, let's get information about the system
    print(f"Created a star system with {len(solar_system)} objects")

    # Print information about the star
    star = solar_system[0]
    star_comp = star.get_component(StarComponent)
    mass_comp = star.get_component(MassComponent)

    print(f"Primary star:")
    print(f"  - Spectral type: {star_comp.spectral_type.value}")
    print(f"  - Mass: {mass_comp.mass_kg / 1.989e30:.2f} solar masses")
    print(f"  - Temperature: {star_comp.surface_temperature_k:.0f} K")
    print(
        f"  - Luminosity: {star_comp.luminosity_solar:.2f} solar luminosities")

    # Get habitable zone
    inner_hz, outer_hz = star_comp.habitable_zone
    print(f"  - Habitable zone: {inner_hz:.2f} AU to {outer_hz:.2f} AU")

    # Print information about planets
    for entity in solar_system[1:]:
        if entity.has_component(OrbitComponent) and entity.has_component(
                MassComponent):
            orbit_comp = entity.get_component(OrbitComponent)
            mass_comp = entity.get_component(MassComponent)

            # Check if this is a planet (orbits the star) or a moon (orbits a planet)
            if orbit_comp.parent_id == star.id:
                print(f"Planet at {orbit_comp.semi_major_axis:.2f} AU:")
                print(
                    f"  - Mass: {mass_comp.mass_kg / 5.972e24:.2f} Earth masses")
                print(
                    f"  - Radius: {mass_comp.radius_km / 6371:.2f} Earth radii")

                # Check if planet is in habitable zone
                in_habitable_zone = inner_hz <= orbit_comp.semi_major_axis <= outer_hz
                if in_habitable_zone:
                    print("  - Located in the habitable zone!")

                # Check for atmosphere
                if entity.has_component(AtmosphereComponent):
                    atmos_comp = entity.get_component(AtmosphereComponent)
                    if atmos_comp.has_atmosphere:
                        print("  - Has atmosphere")
                        if atmos_comp.is_breathable:
                            print("  - Atmosphere is potentially breathable")


if __name__ == "__main__":
    # Run the example
    example_create_solar_system()