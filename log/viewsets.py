from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from log.mixins import ViewTrackingRetrieveModelMixin


class ViewTrackingModelViewSet(mixins.CreateModelMixin,
                               ViewTrackingRetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions. Retrieve action saves viewer in database.
    """
    pass
