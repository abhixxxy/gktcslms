from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('courses/', include('courses.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
