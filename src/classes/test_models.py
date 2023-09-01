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

from unittest import TestCase, main, mock
from models import Person, db_url, Container, Info
import pytest
import datetime


class Testdb(TestCase):
    def test_db_string(self):
        self.assertEqual(type(db_url), str)

    def test_db_file_exists(self):
        self.assertTrue(os.path.exists(db_url))

    def test_db_file_is_file(self):
        self.assertTrue(os.path.isfile(db_url))

    def test_db_file_is_not_dir(self):
        self.assertFalse(os.path.isdir(db_url))


class TestPerson(TestCase):
    def setUp(self) -> None:
        self.person = Person()
        self.person.name = "Pessoa Teste"
        self.person.kg = 60.0
        self.now_drink = 0

    def test_person_instance(self):
        self.assertIsInstance(self.person, Person)

    def test_person_attr_name_is_string(self):
        self.assertEqual(type(self.person.name), str)

    def test_person_attr_kg_is_float(self):
        self.assertEqual(type(self.person.kg), float)

    def test_person_attr_now_drink_is_int(self):
        self.assertEqual(type(self.person.now_drink), int)

    def test_person_attr_kg_is_not_none(self):
        self.assertIsNotNone(self.person.kg)

    def test_person_attr_now_drink_is_not_none(self):
        self.assertIsNotNone(self.person.now_drink)

    def test_person_attr_name_is_not_none(self):
        self.assertIsNotNone(self.person.name)

    def test_person_attr_name_is_not_empty(self):
        self.assertNotEqual(self.person.name, "")

class TestContainer(TestCase):
    def setUp(self) -> None:
        self.container1 = Container()
        self.container2 = Container()
        self.container3 = Container()

        self.container1.title = "Copo pequeno"
        self.container1.capacity = 250
        self.container2.title = "Copo Médio"
        self.container2.capacity = 350.0
        self.container3.title = "Garrafa Média"
        self.container3.capacity = 500.0

    def test_container_instance(self):
        list_containers_ok = []
        list_containers_ok.append(isinstance(self.container1, Container))
        list_containers_ok.append(isinstance(self.container2, Container))
        list_containers_ok.append(isinstance(self.container3, Container))

        self.assertListEqual(list_containers_ok, [1, 1, 1])
    
    def test_container_attr_title_is_string(self):
        list_containers_ok = []
        list_containers_ok.append(type(self.container1.title) == str)
        list_containers_ok.append(type(self.container2.title) == str)
        list_containers_ok.append(type(self.container3.title) == str)

        self.assertListEqual(list_containers_ok, [1, 1, 1])

    def test_container_attr_capacity_know_not_float(self):
        list_containers_not_float = []
        list_containers_not_float.append(type(self.container1.capacity) == float)
        list_containers_not_float.append(type(self.container2.capacity) == float)
        list_containers_not_float.append(type(self.container3.capacity) == float)
        self.assertTrue(not all(list_containers_not_float))

class TestInfo(TestCase):
    def setUp(self) -> None:
        self.info = Info()
        self.info.daily_goal = 2000.0
        self.info.drank = 0.0
        self.info.reached_goal = False
        self.info.created_at = datetime.datetime.now()
        self.info.updated_at = None

    def test_daily_goal_is_float(self):
        self.assertEqual(type(self.info.daily_goal), float)

    def test_daily_goal_is_not_none(self):
        self.assertIsNotNone(self.info.daily_goal)

    def test_drank_is_float(self):
        self.assertEqual(type(self.info.drank), float)

    def test_drank_is_not_none(self):
        self.assertIsNotNone(self.info.drank)

    def test_reach_goal_true(self):
        self.info.drank = 2000.0
        if self.info.drank >= self.info.daily_goal:
            self.info.reached_goal = True
        self.assertTrue(self.info.reached_goal)

    def test_reach_goal_false(self):
        self.info.drank = 1000.0
        if self.info.drank >= self.info.daily_goal:
            self.info.reached_goal = True
        self.assertFalse(self.info.reached_goal)

    def test_created_at_is_datetime(self):
        print("type(self.info.created_at): {}".format(type(self.info.created_at)))
        self.assertEqual(type(self.info.created_at), datetime.datetime)

    def test_created_at_is_not_none(self):
        self.assertIsNotNone(self.info.created_at)

    def test_make_update(self):
        value_ancient = self.info.drank
        self.info.drank += 20.0

        if self.info.drank != value_ancient:
            self.info.updated_at = datetime.datetime.now()
        self.assertIsNotNone(self.info.updated_at)

    def test_create_info(self):
        self.info.drank = 0.0
        self.info.daily_goal = 2001.0
        self.info.reached_goal = None
        self.info.created_at = datetime.datetime.now()

        if self.info.drank is None:
            AssertionError

        if self.info.daily_goal is None:
            AssertionError

        if self.info.reached_goal is None:
            AssertionError

        if self.info.created_at is None:
            AssertionError

        self.assertIsNotNone(self.info.created_at)