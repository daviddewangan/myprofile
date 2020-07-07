from django.db import models



# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200)
    tools = models.CharField(max_length=100) 
    pub_date = models.DateTimeField()
    img_name = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class Webpage(models.Model):
    Username = models.CharField(max_length = 100)
    types = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    message = models.TextField()
    
    
class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    

    
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()
    
SKILLS_CHOICE = (
    ('beginer', 'beg'),
    ('intermediate','inter'),
    ('professional','pro')
    )
    
class Skills(models.Model):
    name = models.CharField(max_length=100)
    exp = models.CharField(choices=SKILLS_CHOICE,max_length=200)
    percent = models.IntegerField()
    
    