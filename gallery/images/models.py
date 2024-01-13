from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/')
    
    def __str__(self):
        return self.title
