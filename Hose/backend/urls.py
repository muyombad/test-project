from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import ProfileView, CreateUserView, LesonsList, CourseProgressView,contact_form


urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')), # Login, Logout, Password Reset, etc.
    
    path('api/register/', CreateUserView.as_view(), name='register'), # just regester.
    path('api/profile/', ProfileView.as_view(), name='profile'), # get and update profile.
    path('lesons/', LesonsList.as_view(), name='lesons'), # get lesons.
    path('progress/', CourseProgressView.as_view(), name='progress'),
    path('api/contact/', contact_form, name='contact_form'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
