from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(default = '', max_length=200)

    product_category = models.CharField(default= '', max_length=200)

    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to= 'uploads/', blank=True, null=True)

    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, default='', editable=False, db_index=True)

    class Meta:
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.product_name
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])


class Category(models.Model):
    product = models.ForeignKey(Product, null = True, related_name = 'categories', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('productapp:category_list', args=[self.slug])
