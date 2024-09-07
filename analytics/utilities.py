import requests

def get_instagram_data(access_token):
    url = 'https://graph.instagram.com/17841469286476544'
    params = {
        'fields': 'id,username,media_count,account_type',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    insta_data = response.json()
    return insta_data

def get_media_data(access_token):
    url = 'https://graph.instagram.com/17841469286476544/media'
    params = {
        'fields': 'id,caption,media_type,media_url,thumbnail_url,permalink',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    media_data = response.json()
    return media_data
