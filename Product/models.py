from django.db import models


class Category(models.Model):
  name = models.CharField(max_length= 100)
  sample = models.ImageField(null=True, blank=True)
  def __str__(self):
    return self.name


# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length = 100)
  item_no = models.CharField(max_length = 40)
  length = models.IntegerField(null=False, blank=False)
  width = models.IntegerField(null=False, blank=False)
  hieght = models.IntegerField(null=False, blank=False)
  finish = models.CharField(max_length = 100)
  material = models.CharField(max_length = 100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  description = models.TextField(blank=True)
  image_1 = models.ImageField()
  image_2 = models.ImageField(null=True, blank=True)
  image_3 = models.ImageField(null=True, blank=True)
  image_4 = models.ImageField(null=True, blank=True)
  def __str__(self):
    return self.name




