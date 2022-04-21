from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename='client')
router.register(r'users', views.UserViewSet)
router.register(r'timelogs', views.TimeLogViewSet)
router.register(r'projects', views.ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('getToken/', TokenObtainPairView.as_view(), name='login'),
    path('refreshToken/', TokenRefreshView.as_view(), name='refresh')
]
