from shop import views
from django.urls import path
app_name="shop"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.allproductcat,name='allproductcat'),
    path('allproducts/<slug:p>',views.allproducts,name='allproducts'),
    path('productdetails/<slug:slug>',views.productdetails,name='productdetails'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.handle_login,name='handle_login'),
    path('logout/',views.handle_logout,name='handle_logout'),

]