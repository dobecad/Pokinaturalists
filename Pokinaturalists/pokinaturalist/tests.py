from django.test import TestCase
from django.db import IntegrityError
from .models import User, Move, Creature, Item

# Create your tests here.


# Database  tests(for local database)
class SqliteDatabaseTests(TestCase):
    @classmethod
    def setUp(cls):
        test = User(token_id="893", username="Ash Ketchum", points=25)
        test.save()

    def test_user_creation(self):
        test2 = User(token_id="6484", username="Gary Oak", points=50)
        test2.save()

    # add a duplicate user test just to be sure of unique status of username
    def test_duplicate_username(self):
        try:
            test2 = User(token_id="8064", username="Ash Ketchum", points=12)
            test2.save()
        except IntegrityError:
            return True
        return False
    def test_move_creation(self):
        test2 = Move(move_name="Thundershock", move_strength=50)
    # add a duplicate move test just to be sure of unique status of username
    def test_duplicate_move(self):
        try:
            test2 = Move(move_name="Thundershock", move_strength=30)
            test3 = Move(move_name="Thundershock", move_strength=50)
            test2.save()
            test3.save()
        except IntegrityError:
            return True
        return False
    def test_creature_creation(self):
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Creature(owner_id=test2, nickname="Pikachu", observation_base="Pokemon num 25", strength=1337)
        test4 = Move(move_name="Thunderbolt", move_strength=42)
        test3.save()
        test4.save()
        test3.moveset.add(test4)

    def test_item_creation(self):
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Item(item_type=1, item_strength=50)
        test3.owner_id = test2

    #user to creatures
    def test_multiple_creature(self):
        # this will test interaction between user and creature by attaching multiple pokemon
        # to the setup of THE POKEMON MASTER(Ash)
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Creature(owner_id=test2, nickname="Pikachu", observation_base="Pokemon num 25", strength=1337)
        test4 = Creature(owner_id=test2, nickname="Charizard", observation_base="Blaze it", strength=420)

    #creature to moves
    def test_multiple_moves(self):
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Creature(owner_id=test2, nickname="Pikachu", observation_base="Pokemon num 25", strength=1337)
        test4 = Move(move_name="Thunderbolt", move_strength=42)
        test5 = Move(move_name="Volt Tackle", move_strength=69)
        test3.save()
        test4.save()
        test5.save()
        test3.moveset.add(test4)
        test3.moveset.add(test5)

    #user to items
    def test_multiple_items(self):
        # let's assume ash has 2 potions
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Item(owner_id=test2, item_type=1, item_strength=50)
        test4 = Item(owner_id=test2, item_type=1, item_strength=50)

#These will be simples tests for the POSTGRES database since SQLite can test rest.
class PostgresDatabaseTests(TestCase):
    @classmethod
    def setUp(cls):
        pass

    def test_creation(self):
        pass

