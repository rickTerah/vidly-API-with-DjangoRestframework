from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
    
        db_table = 'genre'

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
    
        db_table = 'movie'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    class Meta:
    
        db_table = 'customer'

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_returned = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    daily_rental_fee = models.FloatField()

    class Meta:
        db_table = 'rental'
        unique_together = (('movie_id', 'customer_id'),)

