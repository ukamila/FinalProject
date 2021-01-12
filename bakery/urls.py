from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("menu#cakes-section", views.menu, name="menu"),
    path("menu#pastries-section", views.menu, name="menu"),
    path("menu#cookies-section", views.menu, name="menu"),
    path("menu#drinks-section", views.menu, name="menu"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("myorder", views.my_order, name="myorder"),
    path("about", views.about, name="about"),
    path("delivery", views.delivery, name="delivery"),
    path("create", views.create, name="create"),
    path("product/<str:product_id>", views.product, name="product"),
    path("add_to_cart/<str:product_id>", views.add_to_cart, name="add_to_cart"),
    path("orders", views.orders, name="orders"),
    

     #API Routes
     path("checkout", views.checkout, name="checkout"),
     path("completeOrder/<int:order_id>", views.completeOrder, name="completeOrder"),
]