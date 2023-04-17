"""
URL configuration for townhouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from core.views import *

router = SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Endpoints API docs",
    ),
    public=True,

)

router.register(r'source-view-set', SourceViewSet)
router.register(r'status-view-set', StatusViewSet)
router.register(r'card-view-set', CardViewSet)
router.register(r'client-view-set', ClientViewSet)
router.register(r'manager-view-set', ManagerViewSet)
router.register(r'document-view-set', DocumentViewSet)
router.register(r'town-house-view-set', TownHouseViewSet)
router.register(r'construction-view-set', ConstructionViewSet)
router.register(r'locality-view-set', LocalityViewSet)
router.register(r'construction-stage-view-set', ConstructionStageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
