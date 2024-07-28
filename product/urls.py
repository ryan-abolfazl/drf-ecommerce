from django.urls import path, include
from .views import CategoryViewSet, BrandViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('brand', BrandViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]