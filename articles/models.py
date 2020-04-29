from django.db import models

class Article(models.Model):
    """
    Article model
    """
    title = models.CharField('title', max_length=50)
    description = models.TextField('description', max_length=500, default='')
    image_url = models.URLField(null=True)
    
    def __str__(self):
        return self.title