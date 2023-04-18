import django_filters
from django.conf import settings
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from .serializers import *


class CardFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(
        method='filter_by_role', label='nocer_user_rights role')
    all = django_filters.ChoiceFilter(choices=(('true', True), ('false', False)),
                                      method='filter_all', label="'true' or 'false'")

    class Meta:
        model = Card
        fields = ['username']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        """Overwritten method for process filter 'all' if that didn't send """
        if not data.get('all', False):
            copy_data = data.copy()
            copy_data['all'] = 'false'
            super().__init__(copy_data, queryset, request=request, prefix=prefix)
            return
        super().__init__(data, queryset, request=request, prefix=prefix)

    @staticmethod
    def check_auth(request):
        """mock for git"""
        return 'test'

    def is_senior(self) -> bool:
        """Method for getting info about user which logged. And his rank"""
        user = 'test'
        if settings.AUTH:
            user = self.check_auth(self.request)

        user_info = Card.objects.filter(username=user).first() if user else None
        if not user_info:
            raise ValidationError(
                f'User {user} does not exist in table nocer-user')
        return user_info.rank == 'senior'

    def filter_all(self, qs, name, value):
        value = (value in ['true', True])
        if value:
            return qs

        if not self.is_senior():
            qs = qs.filter(rank__iexact='senior')
        return qs

    # def filter_by_role(self, qs, name, value):
    #     qs = qs.filter(
    #         id__in=ReconUserRights.objects
    #         .filter(role=value)
    #         .values('user_id').all()
    #     )
    #     return qs
