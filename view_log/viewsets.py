from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from view_log.mixins import TrackingRetrieveModelMixin


class TrackingModelViewSet(mixins.CreateModelMixin,
                           TrackingRetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions. Retrieve action saves viewer in database.
    """
    pass
