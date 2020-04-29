from django.core.management import BaseCommand
from articles.models import Article
import requests

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads items data from nousdigital endpoint"
    def handle(self, *args, **options):
        URL = "https://cloud.nousdigital.net/s/rNPWPNWKwK7kZcS/download"  
        r = requests.get(url = URL)
        items_data = r.json() 
        for item in items_data["items"]:
            if not Article.objects.filter(title=item["title"]):
                title, description, image_url = item["title"], item["description"], item["imageUrl"]
                article_object = Article(title=title, description=description, image_url=image_url)
                article_object.save()