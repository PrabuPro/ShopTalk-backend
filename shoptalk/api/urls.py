from django.urls import path
from rest_framework import routers
from .views import ItemViewSet, MallViewSet, CategoryViewSet, GetItemsList

router = routers.DefaultRouter()
router.register('api/items', ItemViewSet, 'items')
router.register('api/malls', MallViewSet, 'malls')
router.register('api/categories', CategoryViewSet, 'categories')
# router.register('api/getItems/(?P<mallId>.+)/$', GetItemsList)
urlpatterns = router.urls + [path('api/getItems/<mallId>/', GetItemsList.as_view())]
