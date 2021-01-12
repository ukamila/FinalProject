import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

from .models import User, Product, Order, OrderItem, ItemQuantity

from datetime import datetime, timezone
import pytz
# Create your views here.

def index(request):
    return render(request, "bakery/index.html")

def menu(request):
    cakes = Product.objects.filter(category="CAKES")
    pastries = Product.objects.filter(category="PASTRIES")
    cookies = Product.objects.filter(category="COOKIES")
    drinks = Product.objects.filter(category="DRINKS")
    return render(request, "bakery/menu.html", {
        "cakes" : cakes,
        "pastries" : pastries,
        "cookies" : cookies,
        "drinks" : drinks
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bakery/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "bakery/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        authority = "CUSTOMER"

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "bakery/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.authority = authority
            user.save()
        except IntegrityError:
            return render(request, "bakery/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bakery/register.html")

@login_required
def my_order(request):
    myOrderItems = OrderItem.objects.filter(user=request.user)
    return render(request, "bakery/myorder.html", {
        "products" : myOrderItems
    })

def about(request):
    return render(request, "bakery/about.html")

def delivery(request):
    return render(request, "bakery/delivery.html")

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        ingredients = request.POST['ingredients']
        size = request.POST['size']
        category = request.POST['category']
        category = category.upper()
        image = request.POST['image']
        newProduct = Product(title=title, description=description, price=price, category=category, image=image, ingredients=ingredients, size=size)
        newProduct.save()
        return HttpResponseRedirect(reverse("menu"))
    return render(request, "bakery/create.html")

def product(request, product_id):
    product1 = Product.objects.get(pk=product_id)
    return render(request, "bakery/product.html", {
        "product": product1
    })

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == "POST":
        user = request.user
        quantity = request.POST['quantity']
        price = product.price
        total_price = int(price) * int(quantity)
        newOrderItem = OrderItem(user=user, product=product, quantity=quantity, price=total_price)
        newOrderItem.save()
        return render(request, "bakery/product.html", {
        "product": product
    })
    return render(request, "bakery/product.html", {
        "product": product
    })

@login_required
def orders(request):
    active_orders = Order.objects.filter(active=True)
    inactive_orders = Order.objects.filter(active=False)
    return render(request, "bakery/orders.html", {
        "active_orders": active_orders,
        "inactive_orders": inactive_orders
    })

@csrf_exempt
@login_required
def checkout(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user
        address = data.get("address", "")
        price = data.get("total_price", "")
        total_price = int(price)
        date = datetime.utcnow().replace(tzinfo=pytz.utc)
        newOrder = Order(buyer=user, created_on=date, location=address, total_price=total_price)
        newOrder.save()
        orderItems = OrderItem.objects.filter(user=user)
        for orderItem in orderItems:
            item = ItemQuantity(product=orderItem.product, quantity=orderItem.quantity)
            item.save()
            newOrder.items.add(item)
        newOrder.save()
        OrderItem.objects.filter(user=user).delete()
        return JsonResponse({"message": "success"}, status=201)

@csrf_exempt
@login_required
def completeOrder(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Such order does not exist."}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("active") is not None:
            order.active = data["active"]
        order.save()
        return HttpResponse(status=204)

#.navbar {
 #   overflow: hidden;
 #   position: fixed; /* Set the navbar to fixed position */
 #   top: 0; /* Position the navbar at the top of the page */
  #  width: 100%;
#}