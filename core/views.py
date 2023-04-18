from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from rest_framework.viewsets import ModelViewSet
from .filters import *
from .serializers import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, status


# Create your views here.
class DefaultViewSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'limit'


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.order_by('pk')
    serializer_class = SourceSerializer


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.order_by('pk')
    serializer_class = StatusSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.order_by('pk')
    serializer_class = CardSerializer
    pagination_class = DefaultViewSetPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = CardFilter
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        query_params = self.request.query_params
        page = int(query_params.get('page')) if query_params.get('page') else 1
        limit = int(query_params.get('limit')) if query_params.get('limit') else 50
        order_by = query_params.get('order_by') or 'id'
        order = query_params.get('order') or 'asc'
        order_str = f'-{order_by}' if order == 'desc' else order_by

        queryset = self.filter_queryset(self.get_queryset()).order_by(order_str)
        total = queryset.count()
        serialized = self.get_serializer(
            queryset[(page - 1) * limit:(page - 1) * limit + limit],
            many=True)
        return JsonResponse({
            'pagination': {'limit': limit, 'page': page, 'total': total},
            'content': serialized.data
        })


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.order_by('pk')
    serializer_class = ClientSerializer


class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.order_by('pk')
    serializer_class = ManagerSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.order_by('pk')
    serializer_class = DocumentSerializer


class TownHouseViewSet(ModelViewSet):
    queryset = TownHouse.objects.order_by('pk')
    serializer_class = TownHouseSerializer


class ConstructionViewSet(ModelViewSet):
    queryset = Construction.objects.order_by('pk')
    serializer_class = ConstructionSerializer


class LocalityViewSet(ModelViewSet):
    queryset = Locality.objects.order_by('pk')
    serializer_class = LocalitySerializer


def get_report(data):
    """mock"""
    return data
@swagger_auto_schema(
    method="GET",
    operation_description="Get monitor for date",
    query_serializer=MonitorForDateSerializer,
)
@api_view(['GET'])
def get_date_monitor(request):
    serializer = MonitorForDateSerializer(data=request.GET)
    if not serializer.is_valid():
        return JsonResponse({'error': serializer.errors}, status=400)
    data = serializer.validated_data

    report = get_report(data)
    return JsonResponse(report)

class ConstructionStageViewSet(ModelViewSet):
    queryset = ConstructionStage.objects.order_by('pk')
    serializer_class = ConstructionStageSerializer
