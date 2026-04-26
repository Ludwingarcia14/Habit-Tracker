# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Exponemos los endpoints de nuestra aplicación de hábitos
    path('api/habits/', include('apps.habits.urls')),
]