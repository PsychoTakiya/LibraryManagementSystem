from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    booksName = models.CharField(max_length=322)
    author = models.CharField(max_length=322)
    publisher = models.CharField(max_length=322)