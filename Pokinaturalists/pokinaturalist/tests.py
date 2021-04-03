from django.test import TestCase
from pokinaturalist.models import User, Move, Creature, Item

# Create your tests here.


# Database  tests
# This is wrong, I need to redo these except with actually adding it into the database.
class DatabaseTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test = User(token_id="893", username="Ash Ketchum", points=25)
    def test_user_creation(self):
        test2 = User(token_id="6484", username="Gary Oak", points=50)

    # add a duplicate user test just to be sure of unique status of username
    def test_duplicate_username(self):
        try:
            test2 = User(token_id="8064", username="Ash Ketchum", points=12)
        except IntegrityError:
            return True
        return False
    def test_move_creation(self):
        test2 = Move(move_name="Thundershock", move_strength=50)
    # add a duplicate move test just to be sure of unique status of username
    def test_duplicate_move(self):
        try:
            test2 = Move(move_name="Thundershock", move_strength=30)
        except IntegrityError:
            return True
        return False
    def test_creature_creation(self):
        test2 = Move(move_name="Thundershock", move_strength=30)
        test3 = Creature(owner_id=test, nickname="Pikachu", observation_base="Pokemon num 25", strength=1337)
        test3.moveset.add(test5)

    def test_item_creation(self):
        pass
    def test_user_creature(self):
        pass