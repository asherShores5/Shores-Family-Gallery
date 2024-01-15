from django.db import models
from PIL import Image as PilImage
from django.conf import settings

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/')
    thumbnail = models.ImageField(upload_to='thumbnails/', default='/thumbnails/default.png')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = PilImage.open(self.image.path)
        img.thumbnail((300, 300))
        thumb_path = self.image.path.replace('uploads/', 'thumbnails/')
        img.save(thumb_path)
        self.thumbnail = thumb_path.replace(settings.MEDIA_ROOT, '').lstrip('/')
        super().save(update_fields=['thumbnail'])
    
    def __str__(self):
        return self.title
