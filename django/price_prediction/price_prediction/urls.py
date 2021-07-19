from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('housing/', include('housing.urls')),
    path('admin/', admin.site.urls),
]