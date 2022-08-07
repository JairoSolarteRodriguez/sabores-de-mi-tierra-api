import imp
from posixpath import basename
from rest_framework.routers import DefaultRouter
from api import  views as public_views
from users_app import  views as user_views

router = DefaultRouter()
router.register('category', public_views.CategoryViewSet)
router.register('price', public_views.PriceViewSet)
router.register('utensil', public_views.UtensilViewSet)
router.register('ingredient', public_views.IngredientViewSet)
router.register('measure', public_views.MeasureViewSet)
router.register('difficulty', public_views.DifficultyViewSet)

# User api
router.register('users', user_views.UserViewSet)
router.register('profile', user_views.UserProfileViewSet)

urlpatterns = router.urls
