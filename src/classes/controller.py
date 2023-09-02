try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '.'
            )
        )
    )
except:
    raise


from peewee import *
from models import Person, Container, Info
import json
import datetime
from playhouse.shortcuts import model_to_dict


class ControllerPerson():
    def __init__(self):
        self.person = Person()

    def create(self, name, kg):
        try:
            person = self.person.create(name=name, kg=kg)
            person = json.dumps(model_to_dict(person))
            return person
        except Exception as e:
            raise e

    def get_by_id(self, id):
        try:
            person = self.person.get_or_none(id=id)
            person = json.dumps(model_to_dict(person))
            if person is None:
                return None
            return person
        except Exception as e:
            raise e

    def list_all(self):
        try:
            persons = list(self.person.select().dicts())
            persons = json.dumps(persons)
            return persons
        except Exception as e:
            raise e

    def set_drink(self, person_id, info_id):
        try:
            person = self.person.get_or_none(id=person_id)
            if person is None:
                return None
            person.now_drink = info_id
            person.save()
            print(person.now_drink)
            return True
        except Exception as e:
            raise e


class ControllerInfo():
    def __init__(self):
        self.info = Info()

    def create(self, drank, reached_goal, person_id):
        try:
            person = Person.get_or_none(id=person_id)
            info = self.info.create(
                drank=drank, reached_goal=reached_goal, person=person_id)
            info.daily_goal = person.kg * 35
            person.now_drink = info.id
            info.save()
            person.save()
            info = json.dumps(model_to_dict(
                info), default=ControllerUtils.datetime_handler)
            return info
        except Exception as e:
            raise e

    def get_by_id(self, id):
        try:
            info = self.info.get_or_none(id=id)
            info = json.dumps(model_to_dict(
                info), default=ControllerUtils.datetime_handler)
            if info is None:
                return None
            return info
        except Exception as e:
            raise e

    def list_all(self):
        try:
            infos = list(self.info.select().dicts())
            infos = json.dumps(infos, default=ControllerUtils.datetime_handler)
            return infos
        except Exception as e:
            raise e

    def list_all_by_person(self, person_id):
        try:
            infos = list(self.info.select().where(
                Info.person == person_id).dicts())
            infos = json.dumps(infos, default=ControllerUtils.datetime_handler)
            return infos
        except Exception as e:
            raise e

    def get_info_for_today(self, person_id):
        try:
            info = self.info.get_or_none(
                Info.person == person_id, Info.created_at.day == datetime.datetime.now().day)
            if info is None:
                person = Person.get_or_none(id=person_id)
                info = self.info.create(
                    drank=0, reached_goal=False, person=person_id)
                person.now_drink = info.id
                person.save()
            info = json.dumps(model_to_dict(
                info), default=ControllerUtils.datetime_handler)
            if info is None:
                return None
            return info
        except Exception as e:
            raise e

    def consume_drink(self, info_id, ml):
        try:
            info = self.info.get_or_none(id=info_id)
            if info is None:
                return None
            info.drank += ml
            info.save()

            if info.drank >= info.daily_goal:
                info.reached_goal = True
                info.save()

            info = self.info.get_or_none(id=info_id)

            return {"Drank":info.drank}
        except Exception as e:
            raise e

    def remaning_goal(self, info_id):
        try:
            info = self.info.get_or_none(id=info_id)
            if info is None:
                return None
            return info.daily_goal - info.drank
        except Exception as e:
            raise e

    def remaning_goal_percent(self, info_id):
        try:
            info = self.info.get_or_none(id=info_id)
            if info is None:
                return None
            return (info.drank / info.daily_goal) * 100
        except Exception as e:
            raise e


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

    @staticmethod
    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")
