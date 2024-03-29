from django.db import models


# might make some of these not null requirements just as a protection

# Create your models here.
#User contains Primary, Token, Username, Points, and friendslist
class User(models.Model):
    token_id = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    points = models.IntegerField()
    friendlist = models.ManyToManyField('self')

    class Meta:
        app_label = "pokinaturalist"

# Move contains Primary, name, strength
class Move(models.Model):
    move_name = models.CharField(max_length=25, unique=True)
    move_strength = models.IntegerField()

    class Meta:
        app_label = "pokinaturalist"

#Creature contains primary, link to owner, nickname, observation url, strength and moveset
class Creature(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    #link to icon
    observation_photo = models.CharField(max_length=200)
    observation_wiki = models.CharField(max_length=200)
    strength = models.IntegerField()
    moveset = models.ManyToManyField(Move)

    class Meta:
        app_label = "pokinaturalist"

# Item contains, primary, link to owner, type and strength
class Item(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.IntegerField()
    item_strength = models.IntegerField()

    class Meta:
        app_label = "pokinaturalist"
