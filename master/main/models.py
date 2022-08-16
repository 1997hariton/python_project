from django.db import models

class Task(models.Model):
    title = models.CharField('Название',max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=50)
    image= models.ImageField('images/default.jpg',upload_to='images/')


    def __str__(self):
        return self.title



