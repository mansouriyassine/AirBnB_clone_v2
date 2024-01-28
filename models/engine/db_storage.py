#!/usr/bin/python3
"""Defines the DBStorage class for HBnB project."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

class DBStorage:
    """A class to manage database storage for hbnb models."""
    
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage instance."""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}")

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects of a given type or all types if cls=None."""
        objs = {}
        classes = [State, City, User, Place, Review, Amenity] if cls is None else [cls]
        for cls in classes:
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objs[key] = obj
        return objs


    def reload(self):
        """Reloads the session from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes the session."""
        self.__session.remove()
