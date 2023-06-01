from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=25, unique=True, default='')
    email=models.CharField(max_length=25,default='')
    password=models.CharField(max_length=100,default='')
    SELECTION_CHOICES=(
        ("Grand","Grand"),
        ("NotGrant","NotGrant"),
    )
    user_grand = models.CharField(
        max_length=20,
        choices = SELECTION_CHOICES,
        default = "NotGrant"
    )

    def __str__(self):
        return self.name
class Books(models.Model):
    bname=models.CharField(max_length=50)
    about=models.CharField(max_length=50 ,default='')
    price=models.FloatField()
    author=models.CharField(max_length=25)
    quantity=models.PositiveIntegerField(default='')
    purchased_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.bname
class Buyer(models.Model):
    name = models.ForeignKey(
        Register,
        on_delete=models.CASCADE,
        related_name='buyers'
    )
    bname = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name='buyers'
    )

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Buyer ID: {self.id} - Name: {self.name.name} - Book: {self.bname.bname} - Purchased Quantity: {self.quantity}"
    
class Order(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    bname = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return f"Order ID: {self.id} - Book: {self.bname.bname}"



