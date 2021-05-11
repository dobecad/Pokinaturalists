from django.db import models


# might make some of these not null requirements just as a protection

# Create your models here.
#User contains Primary, Token, Username, Points, and friendslist
class User(models.Model):
    token_id = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    # points should positive
    points = models.IntegerField(default=0)
    friendlist = models.ManyToManyField('self')

    class Meta:
        app_label = "pokinaturalist"

# Move contains Primary, name, strength
class Move(models.Model):
    move_name = models.CharField(max_length=25, unique=True)
    #type is an ENUM: 1:AVIAN , 2:REPTILIAN , 3:MAMMALIAN , 4:FLORA , 5:FUNGI
    move_type = models.IntegerField(default=None)
    move_strength = models.IntegerField(default=20)

    class Meta:
        app_label = "pokinaturalist"

#Creature contains primary, link to owner, nickname, observation url, strength and moveset
#Type, Nickname, ID, owner's ID, photo, photo wiki, strength, def, health, speed, lvl, exp
class Creature(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    #link to icon
    observation_photo = models.CharField(max_length=200)
    observation_wiki = models.CharField(max_length=200)

    #should both be positive
    level = models.IntegerField(default=1)
    experience = models.BigIntegerField(default=0)

    #type is an ENUM: 1:AVIAN , 2:REPTILIAN , 3:MAMMALIAN , 4:FLORA , 5:FUNGI
    type = models.IntegerField(default=None)
    strength = models.IntegerField(default=20)
    defense = models.IntegerField(default=0)
    health = models.IntegerField(default=10)
    speed = models.IntegerField(default=10)

    move = models.ForeignKey(Move, on_delete=models.RESTRICT, blank=True, null=True)

    class Meta:
        app_label = "pokinaturalist"

# Item contains, primary, link to owner, type and strength
class Item(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.IntegerField(default=1)
    item_strength = models.IntegerField(default=20)

    class Meta:
        app_label = "pokinaturalist"
