import requests
import json

fallback_m3u = 'https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/refs/heads/main/assets/moose_na.m3u'
s = requests.session()

def getm3u(streamer):
  url = f'https://pwn.sh/tools/streamapi.py?url='
  try:
    response = s.get(f'{url}{streamer}').json()
    print(f'{streamer=}\n{response}\n\n')
    links = response['urls']
    qualities = {key.replace('p','') if '_' not in key else str(int(key.split('p_')[0])-1) : key for key in links.keys() if key != 'audio_only'}

    quality = sorted(list(map(int, qualities.keys())), reverse=True)[0]
    m3u = links[qualities[str(quality)]]

  except:
    m3u = fallback_m3u
  return m3u

twitch_channels = s.get('https://api.m3use.projectmoose.xyz/channels-twitch').json()
for channel in twitch_channels:
  url = channel.get('url').strip()
  m3u8 = getm3u(url)
  channel['m3u8'] = m3u8

with open ('twitch.json', 'w') as f:
  json.dump(twitch_channels, f, indent=4)
