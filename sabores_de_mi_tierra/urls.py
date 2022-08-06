from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'users/YDJdT640N8Hspnm44867pg0Pcsar3FBQ/', include('users_app.urls')),
    path('api/', include('api.urls')),
]
