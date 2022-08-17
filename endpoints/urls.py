from django.conf.urls import  include


from django.urls import re_path as url






from rest_framework.routers import DefaultRouter

from endpoints.views import EndpointViewSet
from endpoints.views import MLAlgorithmViewSet
from endpoints.views import MLRequestViewSet
from endpoints.views import PredictView  # import PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    # add predict url
    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
]
