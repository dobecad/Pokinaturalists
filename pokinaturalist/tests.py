from django.test import TestCase, Client
from django.core import exceptions
from django.http import HttpRequest
from django.db import IntegrityError
from .models import User, Move, Creature, Item

from . import views
from ipware import get_client_ip

class PokinaturalistAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        del self.client
        return super().tearDown()

    def test_for_valid_ip_addr(self):
        request = HttpRequest()
        request.META = {'HTTP_X_FORWARDED_FOR': '177.139.233.139, 198.84.193.157, 198.84.193.158'}  # From ipware library
        views_ip_addr = views.get_user_ip_addr(request)
        self.assertEqual('177.139.233.139', views_ip_addr)

    def test_index_page_returns_200(self):
        response = self.client.get("/pokinaturalist/")
        self.assertEqual(200, response.status_code)

    def test_ip_addr_stored_in_session(self):
        response = self.client.get("/pokinaturalist/")
        self.assertEqual('127.0.0.1', self.client.session.get("IPv4_ADDR"))

    def test_for_empty_ip_addr(self):
        request = HttpRequest()
        request.META = {}
        self.assertIsNone(views.get_user_ip_addr(request))

# Database  tests(for local database)
class DatabaseTests(TestCase):
    @classmethod
    def setUp(cls):
        test = User(token_id="893", username="Ash Ketchum", points=25)
        test.save()

    # Naive User creation
    def test_user_creation(self):
        test2 = User(token_id="6484", username="Gary Oak", points=50)
        test2.save()
        self.assertEqual(User.objects.get(username="Gary Oak"), test2)

    # add a duplicate user test just to be sure of unique status of username
    def test_duplicate_username(self):
        try:
            test2 = User(token_id="8064", username="Ash Ketchum", points=12)
            test2.save()
        except IntegrityError:
            return True
        return False

    #Naive move creation
    def test_move_creation(self):
        test2 = Move(move_name="Thundershock", move_strength=50)
        test2.save()
        self.assertEqual(Move.objects.get(), test2)

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

    #Naive Creature creation with a move
    def test_creature_creation(self):
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Creature(owner_id=test2, nickname="Pikachu",
                         observation_photo="Shocking", observation_wiki="Pokemon num 25", strength=1337)
        test4 = Move(move_name="Thunderbolt", move_strength=42)
        test3.save()
        test4.save()
        test3.moveset.add(test4)
        self.assertEqual(Creature.objects.get(), test3)

    # Naive Item creation
    def test_item_creation(self):
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Item(item_type=1, item_strength=50)
        test3.owner_id = test2
        test3.save()
        self.assertEqual(Item.objects.get(), test3)

    #Tests multiple creatures to a user
    def test_multiple_creature(self):
        # this will test interaction between user and creature by attaching multiple pokemon
        # to the setup of THE POKEMON MASTER(Ash)
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Creature(owner_id=test2, nickname="Pikachu",
                         observation_photo="Defibrillator", observation_wiki="Pokemon num 25", strength=1337)
        test4 = Creature(owner_id=test2, nickname="Charizard",
                         observation_photo="Blaze it", observation_wiki="Pokemon num 6", strength=420)
        test3.save()
        test4.save()
        self.assertEqual(Creature.objects.filter(owner_id=test2).count(), 2)

    #Tests multiple moves to a creature
    def test_multiple_moves(self):
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Creature(owner_id=test2, nickname="Pikachu",
                         observation_photo="Defibrillator", observation_wiki="Pokemon num 25", strength=1337)
        test4 = Move(move_name="Thunderbolt", move_strength=42)
        test5 = Move(move_name="Volt Tackle", move_strength=69)
        test3.save()
        test4.save()
        test5.save()
        test3.moveset.add(test4)
        test3.moveset.add(test5)
        self.assertEqual(Creature.objects.get(nickname="Pikachu").moveset.count(), 2)

    #Tests multiple items to a user
    def test_multiple_items(self):
        # let's assume ash has 2 potions
        test2 = User.objects.get(username="Ash Ketchum")
        test3 = Item(owner_id=test2, item_type=1, item_strength=50)
        test4 = Item(owner_id=test2, item_type=1, item_strength=50)
        test3.save()
        test4.save()
        self.assertEqual(Item.objects.filter(owner_id=test2).count(), 2)

