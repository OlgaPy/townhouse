from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
from .filters import *
from .utils.util import DefaultViewSetPagination


class BaseFilesViewSet(ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BaseViewSet(ModelViewSet):
    pagination_class = DefaultViewSetPagination
    filter_backends = (DjangoFilterBackend,)

    def list(self, request: Request, *args, **kwargs) -> JsonResponse:
        """Overrated method with default pagination, limit, order"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
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
    # filterset_class = SourceFilter
    http_method_names = ['get', 'post']

    # @swagger_auto_schema(request_body=SourceSerializer,
    #                      responses={
    #                          "200": SourceSerializer(),
    #                          "400": "Bad request params",
    #                          "500": "Server error",
    #                      }, )
    @method_decorator(name='list', decorator=swagger_auto_schema(
        # request_body=SourceSerializer,
        query_serializer=SourceSerializer,
        responses={
            "200": SourceSerializer(),
            "400": "Bad request params",
            "500": "Server error",
        },

        operation_description="description from swagger_auto_schema via method_decorator"
    ))
    def list(self, request: Request, *args, **kwargs) -> JsonResponse:
        super(SourceViewSet, self).list(request, *args, **kwargs)


class StatusViewSet(BaseViewSet):
    queryset = Status.objects.order_by('pk')
    serializer_class = StatusSerializer
    filterset_class = StatusFilter
    http_method_names = ['get', 'post']


class CardViewSet(BaseViewSet):
    queryset = Card.objects.order_by('pk')
    serializer_class = CardSerializer
    filterset_class = CardFilter


class ClientViewSet(BaseViewSet):
    queryset = Client.objects.order_by('pk')
    serializer_class = ClientSerializer
    filterset_class = ClientFilter


class ManagerViewSet(BaseViewSet):
    queryset = Manager.objects.order_by('pk')
    serializer_class = ManagerSerializer
    filterset_class = ManagerFilter


class DocumentViewSet(BaseFilesViewSet):
    queryset = Document.objects.order_by('pk')
    serializer_class = DocumentSerializer
    filterset_class = DocumentFilter


class TownHouseViewSet(BaseViewSet):
    queryset = TownHouse.objects.order_by('pk')
    serializer_class = TownHouseSerializer
    filterset_class = TownHouseFilter


class ConstructionViewSet(BaseFilesViewSet):
    queryset = Construction.objects.order_by('pk')
    serializer_class = ConstructionSerializer
    filterset_class = ConstructionFilter


class LocalityViewSet(BaseViewSet):
    queryset = Locality.objects.order_by('pk')
    serializer_class = LocalitySerializer
    filterset_class = LocalityFilter


class ConstructionStageViewSet(BaseViewSet):
    queryset = ConstructionStage.objects.order_by('pk')
    serializer_class = ConstructionStageSerializer
    filterset_class = ConstructionStageFilter
