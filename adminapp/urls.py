from django.urls import path
from . import views 
# from .views import category_list, category_detail
# from .views import list_users  # Ensure this view is imported
# from .views import complaints  # Ensure this view is imported
from adminapp.views import *
# from .views import category_list, edit_category, delete_category
from django.urls import path
# from .views import complaints_list, assign_officer
from django.urls import path
# from .views import available_officers
from django.urls import path
# from .views import edit_officer, delete_officer
from django.urls import path
# from .views import officer_list  # Import the view

urlpatterns = [
    path('', views.admin_login, name='admin_login'),  # Base URL -> Login Page
    path('admin_index/', views.admin_index, name='admin_index'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path("add-category/", add_category, name="add_category"),
    path("categories/", category_list, name="category_list"),
    path("edit-category/<int:category_id>/", edit_category, name="edit_category"),
    path("delete-category/<int:category_id>/", delete_category, name="delete_category"),
    path('add_officer/', views.add_officer, name='add_officer'),
    path('officers/', views.list_officers, name='list_officers'),
    path('officers/edit/<int:officer_id>/', views.edit_officer, name='edit_officer'),
    path('officers/delete/<int:officer_id>/', views.delete_officer, name='delete_officer'),
    path('list_users/', list_users, name='list_users'),
    path('complaints/', views.admin_complaints_view, name='admin_complaints_list'),
     path('assign_officer/<int:complaint_id>/', assign_officer, name='assign_officer'),
     path('assigned_complaints/', assigned_complaints_view, name='assigned_complaints'),
     path('feedbacks/', admin_feedback_list, name='admin_feedback_list'),
        
]