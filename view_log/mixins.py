from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response

from view_log.models import ViewLog


class TrackingRetrieveModelMixin(RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ViewLog.objects.track_view(instance, self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
