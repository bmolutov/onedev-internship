from django.urls import path

from user_profile.views import ProfileViewSet


urlpatterns = [
    path('get/<email>/', ProfileViewSet.as_view({'get': 'get'})),
    path('edit/<email>/', ProfileViewSet.as_view({'put': 'edit'}))
]
