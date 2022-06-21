from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'created_date']