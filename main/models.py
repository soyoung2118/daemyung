from django.db import models

# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to="pics/carousel_image/")
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title