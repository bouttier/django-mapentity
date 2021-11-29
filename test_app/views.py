from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from mapentity import views as mapentity_views
from mapentity.views import MapEntityViewSet, LastModifiedMixin

from .models import DummyModel
from .serializers import DummySerializer, DummyGeojsonSerializer


class DummyList(mapentity_views.MapEntityList):
    model = DummyModel


class DummyLayer(mapentity_views.MapEntityLayer):
    model = DummyModel


class DummyJsonList(mapentity_views.MapEntityJsonList, DummyList):
    pass


class DummyFormat(mapentity_views.MapEntityFormat):
    model = DummyModel


class DummyDocumentOdt(mapentity_views.MapEntityDocumentOdt):
    model = DummyModel


class DummyDocumentWeasyprint(mapentity_views.MapEntityDocumentWeasyprint):
    model = DummyModel


class DummyDetail(LastModifiedMixin, mapentity_views.MapEntityDetail):
    model = DummyModel


class DummyCreate(mapentity_views.MapEntityCreate):
    model = DummyModel


class DummyUpdate(mapentity_views.MapEntityUpdate):
    model = DummyModel


class DummyDelete(mapentity_views.MapEntityDelete):
    model = DummyModel


class DummyViewSet(MapEntityViewSet):
    model = DummyModel
    queryset = DummyModel.objects.all()
    serializer_class = DummySerializer
    geojson_serializer_class = DummyGeojsonSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
