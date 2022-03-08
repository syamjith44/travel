from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return self.title

