from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.get_cv, name='cv'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
    path('draft/', views.draft, name='draft'),
    path('projects/', views.projects, name='projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('projects/delete/<int:id>', views.delete, name='delete'),
    path('pdf', views.pdf, name='pdf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
