import dailymotion

from requests_toolbelt import MultipartEncoder
import requests


d = dailymotion.Dailymotion()
d.set_grant_type('password', api_key="...", api_secret="..",
    scope=['manage_videos'], info={'username': "...", 'password': "..."})
url = d.upload('./xmas3_short.mp4')


'''
# upload one video = number 000
c = 000
up = d.post('/me/videos',
        {'url': url, 'title': 'Video '+ str(c), 'published': 'true', 'channel': 'tech','is_created_for_kids': 'false'})
print (up['id'])
'''



# upload 250 video
while c < 250:
up = d.post('/me/videos',
        {'url': url, 'title': 'Video '+ str(c), 'published': 'true', 'channel': 'tech','is_created_for_kids': 'false'})
print (up['id'])
    c = c + 1




#video_id = (up['private_id'])
#print ("is done")
