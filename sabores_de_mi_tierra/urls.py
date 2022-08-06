from django.contrib import admin
from django.urls import path, include
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env()
API_KEY = env('API_KEY')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'users/{API_KEY}/', include('users_app.urls')),
    path('api/', include('api.urls')),
]
