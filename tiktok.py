import json
from TikTokApi import TikTokApi
api = TikTokApi()

username = 'andreas.py'



def simple_dict(tiktok_dict):
  to_return = {}
  to_return['user_name'] = tiktok_dict['author']['uniqueId']
  to_return['video_id'] = tiktok_dict['id']
  to_return['video_desc'] = tiktok_dict['desc']
  to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'], to_return['video_id'])

  return to_return

liked_videos = api.userLikedbyUsername(username,count= 1000)
liked_videos = [simple_dict(v) for v in liked_videos]

with open('TikToks.txt','w'):
  f.write('')

for vid_info in liked_videos:
  with open('TikToks.txt','a') as f:
    f.write(json.dumps(vid_info))
    f.write('\n')


  
