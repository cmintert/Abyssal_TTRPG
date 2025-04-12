from dataclasses import dataclass, field
import uuid
from typing import Dict, List, Type, TypeVar, Optional, Set, Any
from abc import ABC, abstractmethod


# Component base class
class Component(ABC):
    """Base class for all components in the ECS system."""
    pass


# Type variable for type hinting
T = TypeVar('T', bound=Component)


class Entity:
    """
    Represents an object in the ECS system.
    An entity is a container for components,
    which define its behaviour and properties.
    """

    def __init__(self, entity_id: Optional[str] = None):
        # Generate a unique ID if none is provided
        self.id = entity_id if entity_id else str(uuid.uuid4())
        self._components: Dict[Type[Component], Component] = {}

    def add_component(self, component: Component) -> None:
        """Add a component to this entity."""
        component_type = type(component)
        self._components[component_type] = component

    def remove_component(self, component_type: Type[Component]) -> None:
        """Remove a component from this entity."""
        if component_type in self._components:
            del self._components[component_type]

    def get_component(self, component_type: Type[T]) -> Optional[T]:
        """Get a component of the specified type if it exists."""
        return self._components.get(component_type)

    def has_component(self, component_type: Type[Component]) -> bool:
        """Check if entity has a component of the specified type."""
        return component_type in self._components


class System(ABC):
    """
    Base class for all systems in the ECS architecture.

    Systems contain the logic to process entities with specific components.
    """

    @abstractmethod
    def update(self, dt: float) -> None:
        """
        Update the system state.
        Args:
            dt: Delta time (time elapsed since the last update)
        """
        pass


class World:
    """
    Container for all entities and systems in the ECS architecture.

    The World manages the creation, retrieval, and deletion of entities,
    as well as the execution of systems.
    """

    def __init__(self):
        self._entities: Dict[str, Entity] = {}
        self._systems: List[System] = []

        # For efficient entity retrieval by component type
        self._component_to_entities: Dict[Type[Component], Set[str]] = {}

    def create_entity(self, entity_id: Optional[str] = None) -> Entity:
        """Create a new entity and add it to the world."""
        entity = Entity(entity_id)
        self._entities[entity.id] = entity
        return entity

    def delete_entity(self, entity_id: str) -> None:
        """Remove an entity and all its components from the world."""
        if entity_id in self._entities:
            entity = self._entities[entity_id]

            # Remove entity from component indices
            for component_type in list(entity._components.keys()):
                if component_type in self._component_to_entities:
                    self._component_to_entities[component_type].discard(
                        entity_id)

            # Remove the entity
            del self._entities[entity_id]

    def add_system(self, system: System) -> None:
        """Add a system to the world."""
        self._systems.append(system)

    def get_entities_with_component(self, component_type: Type[Component]) -> \
            List[Entity]:
        """Get all entities that have a component of the specified type."""
        if component_type not in self._component_to_entities:
            return []

        return [self._entities[entity_id] for entity_id in
                self._component_to_entities[component_type]
                if entity_id in self._entities]

    def get_entity(self, entity_id: str) -> Optional[Entity]:
        """Get an entity by its ID."""
        return self._entities.get(entity_id)

    def update(self, dt: float) -> None:
        """Update all systems."""
        for system in self._systems:
            system.update(dt)

    def _register_component(self, entity: Entity,
                            component_type: Type[Component]) -> None:
        """Register that an entity has a specific component type."""
        if component_type not in self._component_to_entities:
            self._component_to_entities[component_type] = set()

        self._component_to_entities[component_type].add(entity.id)
