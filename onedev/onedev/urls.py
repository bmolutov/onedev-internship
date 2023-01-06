"""onedev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = []


custom_urlpatterns = [
    # custom url patterns
    path('auth/', include('custom_auth.urls')),
    path('profile/', include('user_profile.urls')),
]
urlpatterns.extend(custom_urlpatterns)


drf_patterns = [
    # drf
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns.extend(drf_patterns)


jwt_urlpatterns = [
    # simple jwt
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns.extend(jwt_urlpatterns)


drf_spectacular_urlpatterns = [
    # drf-spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
urlpatterns.extend(drf_spectacular_urlpatterns)


django_urlpatterns = [
    # django
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.extend(django_urlpatterns)
