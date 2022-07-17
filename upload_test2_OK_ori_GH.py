import dailymotion

from requests_toolbelt import MultipartEncoder
import requests


d = dailymotion.Dailymotion()
d.set_grant_type('password', api_key="...", api_secret="....",
    scope=['manage_videos'], info={'username': "...", 'password': "..."})
url = d.upload('./test.mp4')
up = d.post('/me/videos',
    {'url': url, 'title': 'MyTitle', 'published': 'true', 'channel': 'news','is_created_for_kids': 'false'})






print (up)
#video_id = (up['private_id'])
#print ("is done")
