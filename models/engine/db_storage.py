#!/usr/bin/python3
"""
Module for DBStorage class handling SQLAlchemy and MySQL database storage.
"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ


class DBStorage:
    """Storage for database using SQLAlchemy and MySQL."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance."""
        sql_user = environ.get('HBNB_MYSQL_USER', 'root')
        sql_pwd = environ.get('HBNB_MYSQL_PWD', '')
        sql_host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        sql_db = environ.get('HBNB_MYSQL_DB', 'hbnb_dev')
        sql_env = environ.get('HBNB_ENV', 'development')

        self.__engine = create_engine(
                f'mysql+mysqldb://{sql_user}:{sql_pwd}@{sql_host}/{sql_db}',
                pool_pre_ping=True
        )

        if sql_env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Retrieve a dictionary of models currently in storage."""
        session = self.__session

        if not cls:
            tables = [User, State, City, Amenity, Place, Review]
        else:
            tables = [cls]

        obj_dict = {}
        for table in tables:
            query_result = session.query(table).all()

            for row in query_result:
                key = f"{type(row).__name__}.{row.id}"
                obj_dict[key] = row

        return obj_dict

    def new(self, obj):
        """Add a new object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and creates current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session."""
        self.__session.close()
