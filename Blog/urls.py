from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import BlogViewSet, CustomUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'posts', BlogViewSet, basename='posts')
router.register(r'profile', CustomUserViewSet, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('app.urls')),  # your app-specific URLs if any

    # JWT auth endpoints
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
