from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Officer(models.Model):
    Fullname = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)
    Gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    id_card = models.ImageField(null=True, blank=True, upload_to='id_cards/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    officer_id = models.CharField(max_length=255)
    profile = models.ImageField(null=True, blank=True, upload_to='profiles/')

    def __str__(self):
        return self.Fullname