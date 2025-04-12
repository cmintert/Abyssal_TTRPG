from typing import List, Dict, Set, Type
import math
from ECS_Structure import System, Entity, World, Component
from Celestial_Components import (
    MassComponent,
    SystemPositionComponent,
    OrbitComponent,
    StarComponent
)

# Universal gravitational constant (G) in AU^3 kg^-1 day^-2
# Converted from the standard G = 6.67430e-11 m^3 kg^-1 s^-2
G = 1.481e-34  # Approximate value would need precise conversion


class OrbitSystem(System):
    """
    System for updating positions based on orbital parameters.

    This system processes entities with OrbitComponent and SystemPositionComponent,
    calculating their positions based on their orbital elements.
    """

    def __init__(self, world: World):
        self.world = world

    def update(self, dt: float) -> None:
        """
        Update positions based on orbital parameters.

        Args:
            dt: Time step in simulation days
        """
        # Get all entities with both orbit and position components
        entities_with_orbit = self.world.get_entities_with_component(
            OrbitComponent)

        current_time = 0.0  # This would be replaced with a simulation time tracker

        for entity in entities_with_orbit:
            orbit_component = entity.get_component(OrbitComponent)
            position_component = entity.get_component(SystemPositionComponent)

            if not position_component:
                continue

            # Calculate a new position based on orbit
            x, y, z = orbit_component.calculate_position(current_time)

            # Update position
            position_component.x = x
            position_component.y = y
            position_component.z = z


class GravitySystem(System):
    """
    System for calculating gravitational interactions between celestial bodies.

    This system applies N-body gravitational forces between all entities with
    mass and position components.
    """

    def __init__(self, world: World):
        self.world = world

    def update(self, dt: float) -> None:
        """
        Update velocities and positions based on gravitational forces.

        This is a simplified implementation. A real one would use a numerical
        integrator like RK4 or Leapfrog for better accuracy and stability.

        Args:
            dt: Time step in simulation days
        """
        # In a full implementation, we would:
        # 1. Calculate forces between all bodies
        # 2. Update velocities based on forces
        # 3. Update positions based on velocities

        # This is placeholder code to demonstrate the concept
        entities_with_mass = self.world.get_entities_with_component(
            MassComponent)
        entities_with_position = self.world.get_entities_with_component(
            SystemPositionComponent)

        # Find entities with both mass and position
        bodies = [entity for entity in entities_with_mass
                  if entity.has_component(SystemPositionComponent)]

        # Calculate forces (pseudo-code)
        for i, body1 in enumerate(bodies):
            mass1 = body1.get_component(MassComponent).mass_kg
            pos1 = body1.get_component(SystemPositionComponent)

            for j in range(i + 1, len(bodies)):
                body2 = bodies[j]
                mass2 = body2.get_component(MassComponent).mass_kg
                pos2 = body2.get_component(SystemPositionComponent)

                # Calculate distance
                dx = pos2.x - pos1.x
                dy = pos2.y - pos1.y
                dz = pos2.z - pos1.z
                distance = math.sqrt(dx * dx + dy * dy + dz * dz)

                # Calculate gravitational force
                if distance > 0:
                    force_magnitude = G * mass1 * mass2 / (distance * distance)

                    # Apply force to update velocities
                    # In a real implementation, we would have velocity components
                    # and would apply forces to change velocities


class HabitabilitySystem(System):
    """
    System for analysing the habitability of planets.

    This determines if planets are in the habitable zone of their stars and
    calculates habitability scores based on various factors.
    """

    def __init__(self, world: World):
        self.world = world

    def update(self, dt: float) -> None:
        """
        Update habitability calculations for planets.

        Args:
            dt: Time step (not used for this system)
        """
        # Get all stars
        stars = self.world.get_entities_with_component(StarComponent)

        # For each star, find planets and check if they're in the habitable zone
        for star_entity in stars:
            star_component = star_entity.get_component(StarComponent)
            star_position = star_entity.get_component(SystemPositionComponent)

            if not star_position:
                continue

            # Get habitable zone boundaries
            inner_hz, outer_hz = star_component.habitable_zone

            # Get all entities with mass and position components (potential planets)
            planets = self.world.get_entities_with_component(MassComponent)
            planets = [p for p in planets if
                       p.has_component(SystemPositionComponent)]

            for planet_entity in planets:
                # Skip the star itself
                if planet_entity.id == star_entity.id:
                    continue

                planet_position = planet_entity.get_component(
                    SystemPositionComponent)

                # Calculate distance to star
                distance = planet_position.distance_to(star_position)

                # Check if the planet is in the habitable zone
                is_in_habitable_zone = inner_hz <= distance <= outer_hz

                # This is where we would store the habitability result
                # In a real implementation, we would have a HabitabilityComponent
                # to store this information

                # For now, we'll just print the result
                print(
                    f"Planet {planet_entity.id} is {'in' if is_in_habitable_zone else 'outside'} "
                    f"the habitable zone of star {star_entity.id}")


class TimeSystem(System):
    """
    System for managing simulation time.

    This system handles time progression, scaling, and control.
    """

    def __init__(self, world: World, initial_time: float = 0.0,
                 time_scale: float = 1.0):
        self.world = world
        self.current_time = initial_time  # Current simulation time
        self.time_scale = time_scale  # This is how fast simulation time passes relative to real time
        self.paused = False

    def update(self, dt: float) -> None:
        """
        Update the simulation time.

        Args:
            dt: Real time elapsed since the last update (in seconds)
        """
        if not self.paused:
            # Convert real seconds to simulation days with a timescale
            sim_time_delta = dt * self.time_scale / (
                        24 * 3600)  # Convert to days
            self.current_time += sim_time_delta

    def pause(self) -> None:
        """Pause the simulation."""
        self.paused = True

    def resume(self) -> None:
        """Resume the simulation."""
        self.paused = False

    def set_time_scale(self, scale: float) -> None:
        """Set the timescale factor."""
        if scale >= 0:
            self.time_scale = scale

    def get_current_time(self) -> float:
        """Get the current simulation time measured in days."""
        return self.current_time