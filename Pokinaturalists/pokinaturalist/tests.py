from django.test import TestCase
from pokinaturalist.models import User

# Create your tests here.


# Database  tests
class DatabaseTests(TestCase):
    def test_user_creation(self):
        test = User(token_id = "893", username = "Ash Ketchum", points = 25)
        test.save()
        test2 = User(token_id = "6484", username = "Gary Oak", points = 50)
        test2.save()
        print(User.objects.all())
        test.delete()
        test2.delete()
    def test_move_creation(self):
        pass
    def test_creature_creation(self):
        pass
    def test_item_creation(self):
        pass
    def test_user_creature(self):
        pass