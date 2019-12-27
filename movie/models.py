from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    tag_list = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title