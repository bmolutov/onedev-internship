from django.urls import path

from custom_auth.views import RegisterViewSet


urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post': 'register'}), name='register')
]
