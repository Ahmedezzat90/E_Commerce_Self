from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# create a model for cart in e commerce


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        # Check if a Cart already exists for the user
        if not Cart.objects.filter(user=instance).exists():
            Cart.objects.create(user=instance)