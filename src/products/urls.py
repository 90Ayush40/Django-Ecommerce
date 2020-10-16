
from django.urls import path, re_path



from .views import (
    ProductListView, 
    # product_list_view, 
    # ProductDetailView, 
    # product_detail_view,
    ProductDetailSlugView
    # ProductFeaturedListView,
    # ProductFeaturedDetailView
)

urlpatterns = [
    path('', ProductListView.as_view() , name = "productslistview"),
    # path('products-fbv/', product_list_view, name = "products-fbv"),
    # path('featured/', ProductFeaturedListView.as_view(), name = "productsfeatured-list"),
    # # re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name = "productsfeatured-detail"),

    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view() , name = "productsdetailview"),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view() , name = "detail"),
    # re_path(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view, name = "products-detail-fbv")
]
# app_name = 'product'
