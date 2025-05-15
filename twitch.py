import requests
import json

fallback_m3u = 'https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/refs/heads/main/assets/moose_na.m3u'
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.6261.70 Safari/537.36 Edg/122.0.2365.80",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/122.0.6261.70 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
]

s = requests.session()
s.headers['User-Agent'] = random.choice(USER_AGENTS)

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
total = len(twitch_channels)
print(f'{total} twitch channels found')
count = 0
for channel in twitch_channels:
  count += 1
  url = channel.get('url').strip()
  print(f'{count}: {url}')
  m3u8 = getm3u(url)
  channel['m3u8'] = m3u8

with open ('twitch.json', 'w') as f:
  json.dump(twitch_channels, f, indent=4)
