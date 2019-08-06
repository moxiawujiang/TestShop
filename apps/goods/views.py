from rest_framework import generics,viewsets,filters,mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

# Create your views here.

from .models import  Goods,GoodsCategory
from  goods.serializers import GoodsSerializer,CategorySerializer
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = 'Page'
    max_page_size = 100

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    商品列表
    """
    queryset=Goods.objects.all()
    serializer_class =GoodsSerializer
    pagination_class = GoodsPagination
    #authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name','goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

#mixins.RetrieveModelMixin用来获取具体某一个分类
class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    商品分类
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class =CategorySerializer
