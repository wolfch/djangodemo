from django.db import models

# Create your models here.

class Config(models.Model):
    db_username = models.CharField(max_length=200)
    db_password = models.CharField(max_length=200)
    db_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.db_username + ": " + db_url

class Collection(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ": " + self.alias
