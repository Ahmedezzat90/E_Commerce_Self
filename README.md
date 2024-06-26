# E_Commerce_Self
# E-Commerce Website
---------------------------
## Rest-framework (APIS)
- All Products endpoint where I can send query_param to search by name. (product image, name, 
and availability)
- Product details endpoint (product name, image, number of items available, description) 
- Add to cart endpoint
- Get products added to cart per user endpoint
- checkout endpoint where sending email and emptying cart related to this user is handled
- get user info endpoint
- update user info endpoint
- login endpoint using email and password
-signup endpoint ( first_name, last_name, email, password and password confirmation, image not 
mandatory), send confirmation mail upon registering.
- wish-list endpoint that get all products user liked
## Django Templates
### Homepage
- should contain list of products in cards where we can see (product image, name, and 
availability), each card should contain add to cart button.
- Also user should be able to search by name.
### Product Details
- should contain all product’s info (product name, image, number of items available, 
description) and the ability to add it to cart or wish-list.
### Cart page
- should show all the products the user added
- user is able to empty the cart or checkout.
- on checkout send an email to user by the products he/she picked and empty the cart.
### User profile
- should contain registered user info (first name, last name, email, image) *all fields are 
mandatory except image
- user is able to update his/her profile
### Login page
- user can login by email and password *need to take a closer look on django user model and
how to override it ;
### Sign up page
- user must enter first_name, last_name, email, password and password confirmation
- user profile photo is not mandatory to sign up.
- send signup email to user upon registering
### Top bar
- should contain cart for the user to be able to view his/her cart whenever he/she likes
- should contain wish-list in order for user to know the products he/she liked but never 
added to cart
- user should find his/her image or first name on click go to profile info

** for sending emails you may use mail trap
** make sure all views and endpoints only accessible by authenticated users
** user profile, cart, wishlist views and endpoints only accessible by their owner user only
** products should be added/updated or deleted from admin dashboard by admin user
** admin can block normal user from logging to system