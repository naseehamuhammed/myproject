# analytics/social_media_api.py

import requests
from django.utils import timezone
from .models import SocialMediaPost
from django.conf import settings
def fetch_facebook_data():
    # Example function for Facebook API
    access_token = getattr(settings, 'FACEBOOK_ACCESS_TOKEN', None)
  
    url = 'https://graph.facebook.com/me/posts'
    params = {
        'access_token': 'access_token',
        'fields': 'id,message,created_time,likes.summary(true),comments.summary(true)',
    }
    response = requests.get(url, params=params)
    data = response.json()

    for post in data.get('data', []):
        SocialMediaPost.objects.update_or_create(
            platform='Facebook',
            post_id=post['id'],
            defaults={
                'content': post.get('message', ''),
                'likes': post['likes']['summary']['total_count'],
                'shares': 0,  # Assume no share data in this example
                'comments': post['comments']['summary']['total_count'],
                'timestamp': post['created_time'],
            }
        )
def fetch_insta_data():
    # Example function for Facebook API
    url = 'https://graph.instagram.com/17841469286476544/media'
    params = {
        'access_token': 'IGQWRNc0RZARU1sbG1pUkxndzJFRjNqWXNfT2VIMnNMbzZA5U2UyUndQLTRZATVhZAWUhrelBjZATAzenhhWFltb0RNZADBYUF82aHVsbWdBMDJPYmZAScDh2VmN4bHV0dmNJa2gwVE5JVkg3dUZArX0ZASdE56Y1phZAnpCTkUZD',
        'fields': 'id,message,created_time,likes.summary(true),comments.summary(true)',
    }
    response = requests.get(url, params=params)
    data = response.json()

    for post in data.get('data', []):
        SocialMediaPost.objects.update_or_create(
            platform='Instagram',
            post_id=post['id'],
            defaults={
                'content': post.get('message', ''),
                'likes': post['likes']['summary']['total_count'],
                'shares': 0,  # Assume no share data in this example
                'comments': post['comments']['summary']['total_count'],
                'timestamp': post['created_time'],
            }
        )






def fetch_twitter_data():
    # Example function for Twitter API
    url = 'https://api.twitter.com/2/tweets'
    headers = {
        'Authorization': 'Bearer your_twitter_bearer_token',
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    for tweet in data.get('data', []):
        SocialMediaPost.objects.update_or_create(
            platform='Twitter',
            post_id=tweet['id'],
            defaults={
                'content': tweet.get('text', ''),
                'likes': tweet.get('public_metrics', {}).get('like_count', 0),
                'shares': tweet.get('public_metrics', {}).get('retweet_count', 0),
                'comments': tweet.get('public_metrics', {}).get('reply_count', 0),
                'timestamp': timezone.now(),
            }
        )
