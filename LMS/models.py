from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    booksName = models.CharField(max_length=322)
    publisher = models.CharField(max_length=322)
    author = models.CharField(max_length=322)

    def __str__(self):
        return self.booksName

class Readers(models.Model):
    readersName = models.CharField(max_length=322)
    age = models.CharField(max_length=322)

    def __str__(self):
        return self.readersName
    
