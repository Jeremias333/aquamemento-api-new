from unittest import TestCase
from controller import ControllerUtils, ControllerPerson, ControllerInfo, ControllerContainer


class TestControllerUtils(TestCase):
    def test_controller_utils_create_db(self):
        self.assertTrue(ControllerUtils.start_db())

    def test_controller_utils_create_db_at_init(self):
        self.assertTrue(ControllerUtils.start_db(at_init=True))

    def test_initialize_db(self):
        self.assertTrue(ControllerUtils.initialize_db())

    def test_drop_tables(self):
        self.assertTrue(ControllerUtils.delete_all())


class TestControllerPerson(TestCase):
    def setUp(self) -> None:
        self.controller = ControllerPerson()

    def test_list_all(self):
        self.assertIsNotNone(self.controller.list_all())

    def test_get_by_id(self):
        self.assertIsNotNone(self.controller.get_by_id(1))

    def test_create(self):
        self.assertIsNotNone(self.controller.create('teste pessoa', 65))

    def test_set_drink(self):
        self.assertTrue(self.controller.set_drink(1, 1))


class TestControllerInfo(TestCase):
    def setUp(self) -> None:
        self.info = ControllerInfo()

    def test_create(self):
        self.assertIsNotNone(self.info.create(drank=0, reached_goal=False, person_id=1))

    def test_get_by_id(self):
        self.assertIsNotNone(self.info.get_by_id(1))

    def test_list_all(self):
        self.assertIsNotNone(self.info.list_all())


class TestControllerContainer(TestCase):
    def setUp(self) -> None:
        self.controller = ControllerContainer()

    def test_list_all(self):
        self.assertIsNotNone(self.controller.list_all())

    def test_get_by_id(self):
        self.assertIsNotNone(self.controller.get_by_id(1))

    def test_create(self):
        self.assertTrue(self.controller.create('teste', 410))
