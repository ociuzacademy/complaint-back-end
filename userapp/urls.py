from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, loginCreateView,UserComplaintViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# ✅ Setup Router
router = DefaultRouter()
router.register(r'user_complaints', UserComplaintViewSet, basename='user-complaints')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    # ✅ User Registration & Login
    path('userreg/', UserCreateView.as_view(), name='user_register'),
    path('Userlogin/', loginCreateView.as_view(), name='user_login'),
    path('complaints/list/<int:user_id>/', views.list_complaints_by_user, name='list-complaints'),
    path('complaints/<int:pk>/', views.retrieve_complaint, name='retrieve-complaint'),
    path('complaints/delete/<int:pk>/', views.delete_complaint, name='delete-complaint'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    
    # ✅ Include router URLs
    path('', include(router.urls)),

    # ✅ API Schema & Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]
