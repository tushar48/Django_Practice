from django.db import models

# Create your models here.

class Post(models.Model):
    
    post_title = models.CharField(max_length=60) #store less text
    post_content = models.TextField() # storing large text 
    published_date = models.DateTimeField(auto_now=True) # when the object is saved automarically takes the current timing
    

    