from django.urls import path
from . import views

urlpatterns = [
    path("roles/", views.RolesList.as_view()),
    path("roles/<int:pk>", views.RoleDetail.as_view()),
]
