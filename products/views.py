from django.shortcuts import render

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# memo: products/dummy/にアクセスすると、GET, POSTメソッドが確認できる
# クラスベースビュー
class ProductDummyApiView(APIView):
    def get(self, request, format=None):
        # ダミーデータを返却
        return Response({"name": "GET Respose DUMMY!"})

    def post(self, request):
        return Response({"name": "POST Respose DUMMY!"})

product_dummy_api_view = ProductDummyApiView.as_view()


# 関数ベースビュー
@api_view(['GET'])
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)