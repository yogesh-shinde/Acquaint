from django.db import models

# Create your models here.


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=36)
    owner_username = models.CharField(max_length=36)
    owner_password = models.CharField(max_length=36)
    owner_email = models.EmailField()
    owner_contact = models.CharField(max_length=36)

    def __str__(self):
        return self.owner_name
