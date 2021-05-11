from django.contrib import admin
from .models import User, Creature, Move, Item

admin.register(User)
admin.register(Creature)
admin.register(Move)
admin.register(Item)
# Register your models here.
