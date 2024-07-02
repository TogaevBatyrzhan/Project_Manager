from django.db import models

class Subscription(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для хранения цены

    def __str__(self):
        return self.title
