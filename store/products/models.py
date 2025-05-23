from idlelib.debugobj_r import remote_object_tree_item

from users.models import User

from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=256)
    desription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Product: {self.name}, category: {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)



class Basket(models.Model):
     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
     product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField(default=0)
     created_timestamp = models.DateTimeField(auto_now_add=True)

     objects = BasketQuerySet.as_manager()

     def __str__(self):
         return f'Корзина для {self.user.username} | {self.product.name}'

     def sum(self):
         return self.product.price * self.quantity

