from django.db import models
from django.db import models
from django.utils.text import slugify

# Create your models here.

class data(models.Model):
    Name = models.CharField(max_length=150)
    Phone = models.CharField(max_length=50)
    Copies = models.CharField(max_length=50)
    Page_Limit = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)
    Files1 = models.FileField(max_length=2000,null=True,default=None)
    Payment_id= models.CharField(max_length=200)
    Paid = models.BooleanField(default=False)
from django.db import models
from django.utils.text import slugify
class Snippet(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return f'/{self.slug}'    

    


