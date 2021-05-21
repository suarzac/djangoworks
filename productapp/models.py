from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Product(models.Model):
    product_text = models.CharField(max_length=200) 
    product_name = models.CharField(default = '', max_length=200)
    product_category = models.CharField(default= '', max_length=200)
    product_description = models.CharField(default= '', max_length=200)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to= 'uploads/', null=True)

    def __str__(self):
        return self.product_text

    def name(self):
        return f'{self.product_name}'

    def category(self):
        return f'{self.product_category}'

    def description(self):
        return f'{self.product_description}'

    def price(self):
        return f'{self.product_price}'

    def image(self):
        return f'this is image method'