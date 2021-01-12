# Final Project - Bakery

This is my submission for the final project of Web50 course.

## Quick Description

My website is an online store for a bakery, where Users, if signed in, can look through the menu and add products to their shopping cart. Once the items are in shopping cart, the User can proceed to checkout, fill in their address for delivery and place their order. The Staff can then review the orders and mark them as complete if the order was delivered. If the User is not signed in (later referred as a Guest User), they can still look up the menu, see the prices of different items and explore three collections of desserts that are displayed on the homepage: bestsellers, holiday collection and selection of vegan desserts. Lower down on the homepage, the Guest User is encouraged to log in or register, in order to start shopping. 


#### There is nothing to install, this project can be ran the following way

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

## Python files

### admin.py
My admin site works properly, I have created 1 superuser to monitor that the objects were created correctly. You can monitor all 5 models from admin site.

### apps.py
This file configures my app and is quite straight forward.

### models.py
I have stored all my models in this file. Let me go into detail explaining each model.

#### User model
I needed to have a User to make sure that the shopping cart associated with that User can be saved. My User model is fairly simple one, inheriting most of the fields from AbstractUser, except the `Authority Field`, which basically distinguishes Customer User and Staff User, so the Customer can't add a new product to the menu or see Users' orders.
You can sign in as Staff using following credentials : 
username: kamila
password: a2793610A

#### Product model
Since my website sells different desserts and each dessert had data associated with it, I needed to create a Product model which would contain all of that data in different fields. The fields are all different pieces of valuable information about the Product, so the User can see Product's `title`, `description`, `price`, `size`, `ingredients` and `image` and decide whether they want to add it to their cart. The Product model also has a field `category`. I added this field because I wanted for different types of desserts to be separated in different categories. This essentially allowed me to create a Menu with different sections and desserts to be allocated to a section based on their category.

#### OrderItem model
I have ran in a few problems while trying to figure out how to create an Order model, that will contain all information about User's Order. At first I only had 2 models above and 1 Order model, which had the sames fields that it has now, except the `items` field was a ManyToMany relationship with Product model. I soon realized that this won't work because I won't be able to store the quantity and price of each product. Only then I created OrderItem model, which has all that information for each Product that the User adds to their cart. This is only a temporary model, that exists between User adding product to their cart and them placing their order, all the OrderItems associated with that User are then deleted, so the shopping cart says "Your cart is empty".

#### ItemQuantity model
This model also came about only after I have had few issues with my other models. I wanted to delete all User's OrderItems after the checkout, so the User's shopping cart could be emptied after checkout. But before I had this model, Order model was linked to the OrderItems by ManyToMany relationship, so by deleting OrderItems, I would lose all information about the products and their quantities in my Order model. My solution was to create yet another model. This one didn't need to have a User's field or a price field, because all that information would be stored in the Order model. The ItemQuantity model instance is made of two fields, Product and quantity, and is used by Order model instance to show the contents of an Order. 

#### Order model
This model has all information about the User's Order and is viewed by Staff on the orders page. This model's field are `buyer`, `created_on`, `location` - which is the delivery address, `total_price` - the total price of the order, `items` - instances of ItemQuantity model and `active` - a boolean to check whether the order has been completed or not.

### tests.py
My tests.py is empty.

### urls.py
This file contains all of my url paths.

### views.py
All of my views functions are in this file. All of the rendering of templates is happening here.

## Templates

The navigation bar at the top of my website has links to all templates. Every template inherits from layout.html.

### about.html
Simple About page, does not have any functionality, except a heading and a block of text.

### create.html
This template is only accessible by Staff. Here you can fill the form and create a new item that will be shown in the Menu. 

### delivery.html
Another simple page that simply tells that the bakery delivers across the US.

### index.html
This is the homepage and it has three carousels of desserts for three different collections. Hovering a mouse on top of any of the images in a carousel will show the name of the dessert and clicking on the name will redirect you to that dessert's page. At the bottom of the homepage there is a small panel, whose contents change based on whether the User is signed in or not.

### layout.html
Every template inherits from this one. It has the navigation bar and links to stylesheets.

### login.html
This is a login page, where existing Users can log in and start shopping.

### menu.html
This page shows the Menu. There are 4 different sections: `cakes`, `pastries`, `cookies` and `drinks`. In the navigation bar, User can click on any of these sections' names and jump right to the part of the Menu that contains that section, or they can browse the whole Menu. 

### myorder.html
This template is essentialy User's Shopping Cart where all of the products User chose are saved. This page uses JavaScript from myorder.js file. Basically, by clicking "Proceed to Checkout" the shopping cart view is replaced with checking out view where the total price of the order is shown and where the User needs to fill in their delivery address. After they review their order they can click "Checkout" and current view is replaced with the next one saying "Your order was accepted, thank you!". When the User opens their shopping cart again it will say that it is empty, since their order was already placed.

### orders.html 
This page is for Staff to review the orders. There are Active Orders and Completed Orders. When the Staff clicks "Complete" button placed at the bottom of each order, the Order's active field turns to False and the Order can now be found in Completed Orders. This is achieved using 'PUT' method in orders.js.  

### product.html
All of product's information can be found here. A signed in User can also add the product to their cart after specifying the quantity that they want. 

### register.html
This is a page where a Guest User can register. 

## Static Library

All of the photos shown on the homepage are stored here.

There are also these two following files:

### JavaScript Files

myorder.js is used in myorder.html, it calculates the total price of the order, hides and shows different views on click and has 1 POST method that creates a new Order model instance.

orders.js is used in orders.html, it has 1 PUT method that marks an Order as inactive when it is completed.

### styles.css
this css file controls the style of all of the website and makes sure that it is mobile responsive

## Why my project satisfies all of the requirements

I have made my website from scratch and did not base it on any other project from this course. I have not looked into what old CS50W Pizza Project is before working on my final project, therefore I did not realize that my project is similar to it until I almost finished it. My idea is different from Pizza Project and it can be seen based on the structure and design of my website. I have used Django on the back-end and JavaScript on the front-end of my website. I have also added necessary adjustments to my styles.css to make my website mobile responsive.
