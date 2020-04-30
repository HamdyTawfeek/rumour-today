from django.db import models
from django.utils.html import mark_safe
import requests

class Article(models.Model):
    """
    Article model
    """
    title = models.CharField('title', max_length=200)
    description = models.TextField('description', default='',max_length=500)
    image_url = models.URLField(null=True)
    #valid_image = models.BooleanField(default=False)

    def image_tag(self):
        '''
        Image tag to show the image in the admin site
        '''
        return mark_safe(f'<img src="{self.image_url}" alt="Image not found" \
            style="border: 1px solid #000; max-width:250px; max-height:250px;"/>')

    image_tag.short_description = 'Image'
    
    def __str__(self):
        return self.title