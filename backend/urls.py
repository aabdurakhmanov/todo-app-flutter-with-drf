from django.urls import path, include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.TaskList.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]

