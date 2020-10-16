"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include

from django.contrib.auth.views import LogoutView


from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

# from products.views import (
#     ProductListView, 
#     product_list_view, 
#     ProductDetailView, 
#     product_detail_view,
#     ProductDetailSlugView,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView
# )

from accounts.views import login_page, register_page
from .views import home_page,about_page,contact_page


urlpatterns = [
    path('', home_page, name = "home"),
    path('about/', about_page, name = "about"),
    path('contact/', contact_page, name = "contact"),
    path('login/', login_page, name = "login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    # path('cart/', cart_home, name = "cart"),
    path('products/', include("products.urls")),
    path('cart/', include("carts.urls")),
    path('cart/', include("carts.urls", namespace='carts')),
    # path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls")),
    path('search/', include("search.urls", namespace='searches')),
    # path('products/', ProductListView.as_view() , name = "productslistview"),
    # path('products-fbv/', product_list_view, name = "products-fbv"),
    # path('featured/', ProductFeaturedListView.as_view(), name = "productsfeatured-list"),
    # re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name = "productsfeatured-detail"),

    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view() , name = "productsdetailview"),
    # re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view() , name = "productsdetailslugview"),
    # re_path(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view, name = "products-detail-fbv"),

    path('admin/', admin.site.urls),
    path('register/', register_page, name = "register"),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html'))
]

# app_name = 'products'
if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
