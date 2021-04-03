from django.test import TestCase
from pokinaturalist.models import User, Move, Creature, Item

# Create your tests here.


# Database  tests
# This is wrong, I need to redo these except with actually adding it into the database.
# This is great for making sure that this can actually be constructed but it doesn't change the
# issue that I can't really test the multi-attribute parts without actually inserting the models
# into the database. FRUSTRATION
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
        # Need to add ash as owner back when I can add Ash to database(Gary's a poser and placeholder)
        test2 = User(token_id="6484", username="Gary Oak", points=50)
        test3 = Creature(owner_id=test2, nickname="Pikachu", observation_base="Pokemon num 25", strength=1337)
        # test3.moveset.add(test5)

    def test_item_creation(self):
        test2 = Item(item_type=1, item_strength=50)

    #user to creatures
    def test_multiple_creature(self):
        # this will test interaction between user and creature by attaching multiple pokemon
        # to the setup of THE POKEMON MASTER(Ash)
        pass

    #creature to moves
    def test_multiple_moves(self):
        pass

    #user to items
    def test_multiple_items(self):
        pass