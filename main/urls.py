from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)