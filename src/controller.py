from peewee import *
from src.classes.models import Person, Container, Info
import json
import datetime
from playhouse.shortcuts import model_to_dict, dict_to_model


class ControllerPerson():
    pass


class ControllerInfo():
    pass


class ControllerContainer():
    def __init__(self):
        self.container = Container()

    def create(self, title, capacity):
        try:
            container = self.container.create(title=title, capacity=capacity)

            container = json.dumps(model_to_dict(container))
            return container
        except Exception as e:
            raise e

    def get_by_id(self, id):
        try:
            container = self.container.get_or_none(id=id)
            container = json.dumps(model_to_dict(container))
            if container is None:
                return None
            return container
        except Exception as e:
            raise e

    def list_all(self):
        try:
            containers = list(self.container.select().dicts())
            containers = json.dumps(containers)
            return containers
        except Exception as e:
            raise e


class ControllerUtils():
    db_url = 'db.sqlite3'
    db = SqliteDatabase(db_url)

    @classmethod
    def start_db(cls, at_init=False):
        try:
            if at_init:
                cls.db.drop_tables([Person, Container, Info])
            cls.db.create_tables([Person, Container, Info])
            return True
        except Exception as e:
            raise e

    @classmethod
    def initialize_db(cls):
        try:
            cls.start_db(at_init=True)
            cls.create_default_person()
            cls.create_default_containers()
            return True
        except Exception as e:
            raise e

    @classmethod
    def create_default_person(cls):
        try:
            person = Person()
            person.name = "Jeremias Oliveira"
            person.kg = 70.0
            person.save()
            return True
        except Exception as e:
            raise e

    @classmethod
    def create_default_containers(cls):
        try:
            container1 = Container()
            container1.title = "Copo pequeno"
            container1.capacity = 250
            container1.save()

            container2 = Container()
            container2.title = "Copo médio"
            container2.capacity = 350
            container2.save()

            container3 = Container()
            container3.title = "Garrafa média"
            container3.capacity = 500
            container3.save()

            return True
        except Exception as e:
            raise e

    @classmethod
    def delete_all(cls):
        try:
            cls.db.drop_tables([Person, Container, Info])
            return True
        except Exception as e:
            raise e

    @classmethod
    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")
