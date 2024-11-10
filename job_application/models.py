from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    available_date = models.DateField()
    current_status = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
