from django.db.models.deletion import CASCADE
from user.models import User
from django.db import models

class Author(models.Model):
    first_name= models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_by= models.ForeignKey(User, related_name='authors', on_delete=CASCADE)

class Review(models.Model):
    desc= models.TextField()
    rating= models.IntegerField()
    posted_by= models.ForeignKey(User, related_name='reviews', on_delete=CASCADE)

class Book(models.Model):
    title= models.CharField(max_length=45)
    author=models.ForeignKey(Author, related_name='books', on_delete=CASCADE)
    review=models.ManyToManyField(Review)
    added_by=models.ForeignKey(User, related_name='user_books', on_delete=CASCADE)
