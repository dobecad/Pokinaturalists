from django.test import TestCase

from pathlib import Path
from os import path
from os import getenv
from dotenv import load_dotenv
load_dotenv()

class PokinaturalistTestCase(TestCase):
    def test_for_env_file(self):
        self.assertTrue(path.join(Path(__file__).parent.absolute(), ".env"))
    
    def test_for_env_variables(self):
        self.assertIsNotNone(getenv('SECRET_KEY'))