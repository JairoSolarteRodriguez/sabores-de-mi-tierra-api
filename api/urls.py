from api import  views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('price', views.PriceViewSet)
router.register('utensil', views.UtensilViewSet)
router.register('ingredient', views.IngredientViewSet)
router.register('measure', views.MeasureViewSet)
router.register('difficulty', views.DifficultyViewSet)

urlpatterns = router.urls