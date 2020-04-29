from django.db import models
from datetime import datetime
class Realtor(models.Model):
    
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    # this string dunder method is what makes the name show up in the django admin area in the browser. 
    def __str__(self):
        return self.name