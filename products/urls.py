from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductDummyApiView, product_list, product_dummy_api_view

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path("dummy/", ProductDummyApiView.as_view()),
    
    # viewクラスで　product_dummy_api_view = ProductDummyApiView.as_view()とすれば、
    # 関数ベースと同様に使用できる
    path("dummy/", product_dummy_api_view),

    path('list/', product_list),
]