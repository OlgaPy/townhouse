from rest_framework import pagination
import os


class DefaultViewSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'limit'


def get_file_path(instance, filename):
    full_file_path = os.path.join(
        'files/manager_{manager_id}_client_{client_id}/'.format(
            manager_id=instance.manager.id,
            client_id=instance.client.id),
        filename)
    if not os.path.exists(os.path.dirname(full_file_path)):
        os.mkdir(os.path.dirname(full_file_path))
    return full_file_path
