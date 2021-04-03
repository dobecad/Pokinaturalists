from django.db import models

#might make some of these not null requirements just as a protection

# Create your models here.
class User(models.Model):
    token_id = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    points = models.IntegerField()

    class Meta:
        app_label = "User"


class Move(models.Model):
    move_name = models.CharField(max_length=20, unique=True)
    move_strength = models.IntegerField()

    class Meta:
        app_label = "Move"


class Creature(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    # link to the base observation(url?) Can derive picture from that
    observation_base = models.CharField(max_length=200)
    strength = models.IntegerField()
    moveset = models.ManyToManyField(Move)

    class Meta:
        app_label = "Creature"


class Item(models.Model):
    item_type = models.IntegerField()
    item_strength = models.IntegerField()

    class Meta:
        app_label = "Item"