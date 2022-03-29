import factory
from django.contrib.gis.geos import Point

from test_app.models import DummyModel


class DummyModelFactory(factory.django.DjangoModelFactory):
    name = 'a dummy model'

    geom = Point(0, 0)

    class Meta:
        model = DummyModel
