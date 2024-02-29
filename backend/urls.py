from django.urls import path, include
from backend.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('establishment', EstablishmentViewSet, basename='establishment')

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('api/', include(router.urls)),
]
