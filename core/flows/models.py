from django.db import models
from typing import Optional
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Project(models.Model):

    options =(
        ('show', 'Show'),
        ('hide', 'Hide')
    )

    project_name= models.CharField(max_length= 250)
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name="project")
    published_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    slug = models.SlugField(null=True, unique= True)
    image1 = models.ImageField(upload_to = 'images/', null = True, blank= True)


    
    class Meta:
        ordering = ('-published_date',)

    
    def __str__(self):
       return self.project_name 
       
       

    def save(self, *args, **kwargs):
         if not self.slug:
             self.slug = slugify(self.project_name)
         return super().save(*args, **kwargs)  

             