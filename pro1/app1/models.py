from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Books(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length = 200)
    available_status = models.BooleanField(default=True)

    def __str__(self):
        return self.book_name


