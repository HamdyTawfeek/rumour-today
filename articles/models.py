from django.db import models
from django.utils.html import mark_safe


class Article(models.Model):
    """
    Article model
    """
    title = models.CharField('title', max_length=50)
    description = models.TextField('description', max_length=500, default='')
    image_url = models.URLField(null=True)

    def image_tag(self):
        # to show the image in  the admin site
        return mark_safe(f'<img src="{self.image_url}" alt="Image not found" \
            style="border: 1px solid #000; max-width:250px; max-height:250px;"/>')

    image_tag.short_description = 'Image'
    
    def __str__(self):
        return self.title