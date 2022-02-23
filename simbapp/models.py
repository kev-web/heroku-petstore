from django.db import models

# Create your models here.


class CodingPics(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='cool_coding_images')

    class Meta: 
        verbose_name_plural = 'Coding Pics'

    def __str__(self):
        return self.name



class DogInfo(models.Model):
    dog_name = models.CharField(max_length=50)
    dog_age = models.IntegerField()
    dog_owner = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Dog Info'

    def __str__(self):
        return self.dog_name