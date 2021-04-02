from django.db import models


# Create your models here.
class User(models.Model):
    token_id = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    points = models.IntegerField()


class Move(models.Model):
    move_name = models.CharField(max_length=20)
    move_strength = models.IntegerField()


class Creature(models.Model):
    owner_id = models.ForeignKey(User, on_delete=CASCADE)
    nickname = models.CharField(max_length=50)
    # link to the base observation(url?) Can derive picture from that
    observation_base = models.CharField(max_length=200)
    strength = models.IntegerField()
    moveset = models.ManyToManyRel(Move)


class Item(models.Model):
    item_type = models.IntegerField()
    item_strength = models.IntegerField()