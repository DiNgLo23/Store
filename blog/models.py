from django.db import models

def default_photo():
    return "/mysite/images/Noname.png"

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    desc = models.CharField(max_length = 200)
    img = models.ImageField(blank=True,upload_to='images',default=default_photo)
    



    def __str__(self):
        return self.name
    

