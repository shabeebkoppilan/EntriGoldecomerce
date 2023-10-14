
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.allproducts,name="allproducts"),
    path('<slug:slug_c>/', views.allproducts,name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/',views.prod_det,name='product_catdetail'),
    path('cart',views.cart,name="cart"),
    path('payments',views.payments,name="payments"),
    path('profile',views.profile,name="profile"),
]