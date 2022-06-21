from rest_framework import viewsets
from rest_framework import permissions
from person.models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """
    http_method_names = ['get']
    serializer_class = PersonSerializer
    queryset = Person.objects.order_by("-created_date")

    