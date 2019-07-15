from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=250)
    image_url = models.TextField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu_item')

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.name
