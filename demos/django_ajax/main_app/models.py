from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['title']) < 1:
            errors['title'] = 'Title is required!'
        elif len(self.filter(title = post_data['title'])) > 0:
            errors['title'] = 'Product already exist!'
        return errors


class Product(models.Model):
    title = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()