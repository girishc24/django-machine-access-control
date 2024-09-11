from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('api/machines/', views.MachineViewSet.as_view()),
]