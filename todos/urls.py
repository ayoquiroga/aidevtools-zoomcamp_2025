from django.urls import path
from . import views

urlpatterns = [
    path('', views.TODOListView.as_view(), name='todo_list'),
    path('create/', views.TODOCreateView.as_view(), name='todo_create'),
    path('edit/<int:pk>/', views.TODOUpdateView.as_view(), name='todo_edit'),
    path('delete/<int:pk>/', views.TODODeleteView.as_view(), name='todo_delete'),
    path('toggle/<int:pk>/', views.toggle_resolved, name='todo_toggle'),
]
