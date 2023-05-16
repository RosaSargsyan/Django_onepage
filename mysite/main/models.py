from django.db import models

# Create your models here.

class Home(models.Model):
    titl = models.CharField('Title', max_length=100)
    name1 = models.CharField('name1', max_length=100)
    name2 = models.CharField('name2', max_length=100)
    about = models.TextField('about')
    img = models.ImageField('Home img', upload_to='photo')

    def __str__(self) -> str:
        return self.name1
    
class About(models.Model):
    name1 = models.CharField('name1', max_length=100)
    name2 = models.CharField('name2', max_length=100)
    about = models.TextField('about')
    img = models.ImageField('About img', upload_to='photo')
    def __str__(self) -> str:
        return self.name1
    
class Proj(models.Model):
    name = models.CharField('name proj', max_length=100)
    img = models.ImageField('About img', upload_to='photo')
    def __str__(self) -> str:
        return self.name


class Logo(models.Model):
    logo = models.ImageField('logo', upload_to='photo')

class Contact(models.Model):
    # name1 = models.CharField('name proj', max_length=100)
    # about = models.TextField('about')
    name = models.CharField('User name', max_length=100)
    email = models.EmailField('User email')
    message = models.TextField('User review')


