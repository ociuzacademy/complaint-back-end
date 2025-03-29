from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import OfficerLoginView,AssignedComplaintsView,ComplaintStatusViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'update-complaint-status', ComplaintStatusViewSet, basename='complaint-status')

urlpatterns = [
    path('officer/login/', OfficerLoginView.as_view(), name='officer-login'),
    path('assigned-complaints/<str:officer_id>/', AssignedComplaintsView.as_view(), name='assigned-complaints'),


    # Swagger and API documentation routes
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include(router.urls)),
    
]
