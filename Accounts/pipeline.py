import os
import requests
from django.conf import settings

def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = 'https://w7.pngwing.com/pngs/893/926/png-transparent-silhouette-user-icon-profile-silhouette-silhouette-avatar-profile-silhouette-thumbnail.png'
    
    if backend.name == 'facebook':
        url = f"https://graph.facebook.com/{response['id']}/picture?width=600&height=600"
        response = requests.get(url)
        file_name = 'users_avatars/' + url.split('/')[-2] + '.png'

    if backend.name == 'google-oauth2':
        url = response['picture']
        response = requests.get(url)
        file_name = 'users_avatars/' + url.split('/')[-1] + '.png'

    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    if url:
        user.image = file_name
        user.save()