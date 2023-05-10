from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields=('name','url','affiliations','occupations','birthday','anime_debut')