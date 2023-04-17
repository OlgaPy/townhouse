from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class SourceViewSet(ModelViewSet):
    queryset = Source.objects.order_by('pk')
    serializer_class = SourceSerializer


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.order_by('pk')
    serializer_class = StatusSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.order_by('pk')
    serializer_class = CardSerializer


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


class ConstructionStageViewSet(ModelViewSet):
    queryset = ConstructionStage.objects.order_by('pk')
    serializer_class = ConstructionStageSerializer
