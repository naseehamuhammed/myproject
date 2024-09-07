# analytics/management/commands/fetch_social_media_data.py

from django.core.management.base import BaseCommand
from analytics.social_media_api import fetch_facebook_data,fetch_insta_data

class Command(BaseCommand):
    help = 'Fetch social media data and update the database'

    def handle(self, *args, **kwargs):
        fetch_facebook_data()
        fetch_insta_data()
        self.stdout.write(self.style.SUCCESS('Successfully updated social media data'))
