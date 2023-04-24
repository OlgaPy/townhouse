from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .filters import *
from .utils.util import DefaultViewSetPagination


class BaseViewSet(ModelViewSet):
    pagination_class = DefaultViewSetPagination
    filter_backends = (DjangoFilterBackend, )
    http_method_names = ['get', 'post']

    def list(self, request: Request, *args, **kwargs) -> JsonResponse:
        """Overrated method with default pagination, limit, order"""
        query_params = self.request.query_params
        page = int(query_params.get('page')) if query_params.get('page') else 0
        limit = int(query_params.get('limit')) if query_params.get('limit') else 50
        order_by = query_params.get('order_by') or 'id'
        order = query_params.get('order') or 'asc'
        order_str = f'-{order_by}' if order == 'desc' else order_by

        queryset = self.filter_queryset(self.get_queryset()).order_by(order_str)
        total = queryset.count()
        serialized = self.get_serializer(queryset[page * limit:page * limit + limit], many=True)
        return JsonResponse({
            'pagination': {'limit': limit, 'page': page, 'total': total},
            'content': serialized.data
        })


class SourceViewSet(BaseViewSet):
    queryset = Source.objects.order_by('pk')
    serializer_class = SourceSerializer


class StatusViewSet(BaseViewSet):
    queryset = Status.objects.order_by('pk')
    serializer_class = StatusSerializer
    filterset_class = StatusFilter


class CardViewSet(BaseViewSet):
    queryset = Card.objects.order_by('pk')
    serializer_class = CardSerializer


class ClientViewSet(BaseViewSet):
    queryset = Client.objects.order_by('pk')
    serializer_class = ClientSerializer


class ManagerViewSet(BaseViewSet):
    queryset = Manager.objects.order_by('pk')
    serializer_class = ManagerSerializer


class DocumentViewSet(BaseViewSet):
    queryset = Document.objects.order_by('pk')
    serializer_class = DocumentSerializer


class TownHouseViewSet(BaseViewSet):
    queryset = TownHouse.objects.order_by('pk')
    serializer_class = TownHouseSerializer


class ConstructionViewSet(BaseViewSet):
    queryset = Construction.objects.order_by('pk')
    serializer_class = ConstructionSerializer


class LocalityViewSet(BaseViewSet):
    queryset = Locality.objects.order_by('pk')
    serializer_class = LocalitySerializer


class ConstructionStageViewSet(BaseViewSet):
    queryset = ConstructionStage.objects.order_by('pk')
    serializer_class = ConstructionStageSerializer
