from django.contrib import admin
from django.urls import path, include

import environ

from users_app import views
env = environ.Env()

# reading .env file
environ.Env.read_env()

API_KEY = env('API_KEY')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(f'users/{API_KEY}/', include('users_app.urls')),
    path(f'login/{API_KEY}/', views.UserLoginApiView.as_view()),
]
