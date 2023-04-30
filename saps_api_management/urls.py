from django.urls import include, path
from .modules.roles import urls as rolesUrls

# from .views import RolesViewSet

# router = routers.DefaultRouter()
# router.register(r'roles', views.roles_list)

urlpatterns = [
    # path('v1/', include(router.urls))
    path("v1/", include(rolesUrls))
]
