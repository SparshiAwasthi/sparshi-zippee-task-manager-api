#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from .views import TaskViewSet

#router = DefaultRouter()
#router.register(r'tasks', TaskViewSet, basename='task')

#urlpatterns = [
#    path('', include(router.urls)),
#]

from django.urls import path, include
from rest_framework import routers, permissions
from tasks.views import TaskViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Router for TaskViewSet
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# Swagger documentation setup
schema_view = get_schema_view(
   openapi.Info(title="Task Manager API", default_version='v1', description="API documentation for Task Manager",),
   public=True, permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
