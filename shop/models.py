from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}'


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.name} - {self.item.price} - {self.name} - {self.age} - {self.date_purchase}'
