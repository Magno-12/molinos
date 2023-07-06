from rest_framework import routers
from apps.authentication.views.auth_view import AuthViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]
