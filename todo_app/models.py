from django.db import models

# Create your models here.

class todo_table(models.Model):
    todo=models.CharField(max_length=100)
    todo2=models.CharField(max_length=100)
    # completed = models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)


