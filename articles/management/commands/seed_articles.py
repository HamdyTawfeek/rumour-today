from django.core.management import BaseCommand
from articles.models import Article
import requests


def is_url_image(image_url):
    '''
    Check if image url is not broken to decide wether to render it or not!
    '''
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    return False


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads items data from nousdigital endpoint"
    def handle(self, *args, **options):
        URL = "https://cloud.nousdigital.net/s/rNPWPNWKwK7kZcS/download"  
        r = requests.get(url = URL)
        items_data = r.json() 
        for item in items_data["items"]:
            if not Article.objects.filter(title=item["title"]):
                try:
                    title, description, image_url = item["title"], item["description"], item["imageUrl"]
                    valid_image = is_url_image(image_url)
                    article_object = Article(title=title, description=description, image_url=image_url, valid_image=valid_image)
                    article_object.save()
                except:
                    pass