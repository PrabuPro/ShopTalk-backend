from rest_framework import routers
from .views import ItemViewSet, MallViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('api/items', ItemViewSet, 'items')
router.register('api/malls', MallViewSet, 'malls')
router.register('api/categories', CategoryViewSet, 'categories')
urlpatterns = router.urls
