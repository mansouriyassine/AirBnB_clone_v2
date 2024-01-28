#!/usr/bin/python3
"""State class for HBnB project."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """Representation of state for HBnB project."""
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """Returns the list of City instances linked to the State."""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
