from django.db import models
from django.contrib.auth.models import User

class Videogame(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_videogames')

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def save(self, *args, **kwargs):
        self.total_price = self.videogame.price * self.quantity
        super().save(*args, **kwargs)
