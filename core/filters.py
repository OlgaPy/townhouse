import django_filters

from .models import *


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = '__all__'


class StatusFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Status
        fields = ['id', 'name']


class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = '__all__'


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = '__all__'


class ManagerFilter(django_filters.FilterSet):
    class Meta:
        model = Manager
        fields = '__all__'


class DocumentFilter(django_filters.FilterSet):
    file = django_filters.CharFilter(method='filter_file')

    def filter_file(self, qs, name, value):
        return qs.filter(**{'file__icontains': value})

    class Meta:
        model = Document
        fields = ('name', 'client', 'building', 'manager')


class TownHouseFilter(django_filters.FilterSet):
    class Meta:
        model = TownHouse
        fields = '__all__'


class ConstructionFilter(django_filters.FilterSet):
    schema_file = django_filters.CharFilter(method='filter_sf')

    def filter_sf(self, qs, name, value):
        return qs.filter(**{'schema_file__icontains': value})

    class Meta:
        model = Construction
        fields = ('name', 'floor', 'rooms', 'square_house')


class LocalityFilter(django_filters.FilterSet):
    class Meta:
        model = Locality
        fields = '__all__'


class ConstructionStageFilter(django_filters.FilterSet):
    class Meta:
        model = ConstructionStage
        fields = '__all__'
