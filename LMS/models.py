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

class Borrowers(models.Model):
    bId = models.CharField(max_length=322)
    bkName = models.CharField(max_length=322)
    rName = models.CharField(max_length=322)
    bdate = models.DateField(null=True)

    def __str__(self):
        return self.bId
    
