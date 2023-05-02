from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Car(models.Model):
    county_choice = (
        ('Bong','Bong'),
        ('Bomi','Bomi'),
        ('Gbarpolu','Gbarpolu'),
        ('Grand Bassa','Grand Bassa'),
        ('Grand Cape Mount','Grand Cape Mount'),
        ('Grand Gedeh','Grand Gedeh'),
        ('Grand Kru','Grand Kru'),
        ('Lofa','Lofa'),
        ('Margibi','Margibi'),
        ('Maryland','Maryland'),
        ('Montserrado','Montserrado'),
        ('Nimba','Nimba'),
        ('Rivercess','Rivercess'),
        ('River Gee','River Gee'),
        ('Sinoe','Sinoe'),
    )
    
    year_choice = []
    for r in range(2000,(datetime.now().year + 1)):
        year_choice.append((r,r))
    

    id = models.AutoField(primary_key=True)
    car_title = models.CharField(max_length=255)
    county = models.CharField(choices=county_choice, max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.IntegerField()
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price= models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    fuel_type = models.CharField(max_length=50)
    body_type = models.CharField(max_length=100, blank=True, null=True)
    transmission = models.CharField(max_length=100, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.car_title