from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import ProfileView, CreateUserView

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')), # Login, Logout, Password Reset, etc.
    
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
