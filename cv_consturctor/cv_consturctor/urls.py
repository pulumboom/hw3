from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('cv/', include('cv.urls')),
    path('', include('cv.urls'))
]

handler404 = 'cv.views.view_404'
