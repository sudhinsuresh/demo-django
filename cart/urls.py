from cart import views
from django.urls import path
app_name="cart"

urlpatterns = [
    path('add_to_cart/<int:p>/',views.add_to_cart,name="add_to_cart"),
    path('cartview',views.cartview,name='cartview'),
    path('cart_remove/<int:p>/',views.cart_remove,name="cart_remove"),
    path('cart_delete/<int:p>/',views.cart_delete,name="cart_delete"),
    path('orderform',views.orderform,name="orderform"),
    path('order_view',views.order_view,name="order_view"),
    

]