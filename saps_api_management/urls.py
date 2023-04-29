from django.urls import path
from . import views
# from .views import RolesViewSet

# router = routers.DefaultRouter()
# router.register(r'roles', views.roles_list)

urlpatterns = [
    # path('v1/', include(router.urls))
    path('v1/roles/', views.RolesList.as_view())
]
