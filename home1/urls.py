from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('exodest/', include('exodest.urls')),
    path('admin/', admin.site.urls),
]
