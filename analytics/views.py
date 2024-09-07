
# analytics/views.py

from django.shortcuts import render
from .models import SocialMediaPost
from .utilities import get_instagram_data, get_media_data
import requests
from django.conf import settings # Updated to include render
from django.http import JsonResponse
def dashboard(request):
    posts = SocialMediaPost.objects.all()
    access_token = getattr(settings, 'INSTAGRAM_ACCESS_TOKEN', None)
    user_id = getattr(settings, 'INSTAGRAM_USER_ID', None)

    if not access_token or not user_id:
        # Render error message on the dashboard
        return render(request, 'analytics/dashboard.html', {'error': 'Access token or User ID is not found in settings'}, status=400)

    # Instagram Graph API endpoint to fetch recent media from the user's account
    url = f"https://graph.instagram.com/{user_id}/media"
    params = {
        "access_token": access_token,
        "fields": "id,caption,media_type,media_url,thumbnail_url,timestamp",  # Specify the fields you want to fetch
        "limit": 5  # Adjust the limit as needed
    }

    # Making the GET request to the Instagram API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts_data = data.get('data', [])

        # Extract relevant information from the posts data
        posts_info = [{
            'id': post.get('id'),
            'caption': post.get('caption', 'No caption'),
            'media_type': post.get('media_type'),
            'media_url': post.get('media_url'),
            'thumbnail_url': post.get('thumbnail_url') if post.get('media_type') == 'VIDEO' else post.get('media_url'),
            'timestamp': post.get('timestamp')
        } for post in posts_data]

        # Render the posts data in the HTML template
        context = {
        'insta_posts':posts_info ,
        'posts':posts
        }
        return render(request, 'analytics/dashboard.html',  context)
    else:
        # Extract error details and render in the template
        error = response.json().get("error", {})
        return render(request,'analytics/dashboard.html', {'error': f"Error {response.status_code}: {error.get('message')}"}, status=response.status_code)


def dashboard_insta(request):
    access_token = 'IGQWRPUkx0TXZA0QTR1TlhlMm84Mkg4YjRNQnoxME9Ib1VSNW5nbndUX1FCekROaGdJYlpzR3h5Q194WFVURTEwRktmWmpmbE5FcFBXYlJTcHVTNHJINVgzbzNUWUFCRWZA2N0hRc1pucUJLekdqSC1vQ09NOUJETVEZD'
    user_data = get_instagram_data(access_token)
    media_data = get_media_data(access_token)
    
    context = {
        'user_data': user_data,
        'media_data': media_data
    }
    
    return render(request, 'analytics/dashboard.html', context)



