from unittest import TestCase
from controller import ControllerUtils

class TestControllerUtils(TestCase):
    def test_controller_utils_create_db(self):
        self.assertTrue(ControllerUtils.start_db())

    def test_controller_utils_create_db_at_init(self):
        self.assertTrue(ControllerUtils.start_db(at_init=True))
    
    def test_initialize_db(self):
        self.assertTrue(ControllerUtils.initialize_db())