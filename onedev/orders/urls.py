from django.urls import path

from orders.views import OrderViewSet


urlpatterns = [
    path('create/', OrderViewSet.as_view({'post': 'create'})),
    path('list/', OrderViewSet.as_view({'get': 'list'}))
]
