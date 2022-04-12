from .api import (
    MapEntityLayer,
    MapEntityViewSet
)
from .base import (
    ServeAttachment,
    JSSettings,
    map_screenshot,
    history_delete,
)
from .generic import (
    Convert,
    MapEntityList,
    MapEntityFormat,
    MapEntityMapImage,
    MapEntityDocument,
    MapEntityDocumentBase,
    MapEntityDocumentOdt,
    MapEntityDocumentWeasyprint,
    MapEntityMarkupWeasyprint,
    DocumentConvert,
    MapEntityCreate,
    MapEntityDetail,
    MapEntityUpdate,
    MapEntityDelete,
)
from .logentry import LogEntryList, LogEntryViewSet
from .mixins import (
    JSONResponseMixin,
    LastModifiedMixin,
    ModelViewMixin,
)

MAPENTITY_GENERIC_VIEWS = [
    MapEntityLayer,
    MapEntityList,
    MapEntityFormat,
    MapEntityMapImage,
    MapEntityDocument,
    MapEntityMarkupWeasyprint,
    MapEntityCreate,
    MapEntityDetail,
    MapEntityUpdate,
    MapEntityDelete,
]

__all__ = [
    'Convert',
    'MapEntityList',
    'MapEntityFormat',
    'MapEntityMapImage',
    'MapEntityDocument',
    'MapEntityDocumentBase',
    'MapEntityDocumentOdt',
    'MapEntityDocumentWeasyprint',
    'MapEntityMarkupWeasyprint',
    'DocumentConvert',
    'MapEntityCreate',
    'MapEntityDetail',
    'MapEntityUpdate',
    'MapEntityDelete',
    'MapEntityLayer',
    'MapEntityViewSet',
    'JSONResponseMixin',
    'LastModifiedMixin',
    'ModelViewMixin',
    'MAPENTITY_GENERIC_VIEWS',
    'ServeAttachment',
    'JSSettings',
    'map_screenshot',
    'history_delete',
    'LogEntryList',
    'LogEntryViewSet'
]
