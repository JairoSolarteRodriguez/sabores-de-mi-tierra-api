from django.contrib import admin
from users_app import models


admin.site.register(models.User)
admin.site.register(models.Profile)
