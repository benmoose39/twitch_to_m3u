import requests
import json
import random
import time

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

def is_valid_m3u8(url):
    try:
        resp = s.head(url, timeout=5)
        return resp.status_code == 200 and url != fallback_m3u
    except:
        return False

def getm3u(streamer):
    base_url = 'https://pwn.sh/tools/streamapi.py?url='
    try:
        s.headers['User-Agent'] = random.choice(USER_AGENTS)
        response = s.get(f'{base_url}{streamer}', timeout=10).json()
        print(f'{response}')
        print('sleeping for 5 seconds...')
        time.sleep(5)
        links = response['urls']
        qualities = {
            key.replace('p', '') if '_' not in key else str(int(key.split('p_')[0]) - 1): key
            for key in links.keys() if key != 'audio_only'
        }
        quality = sorted(map(int, qualities.keys()), reverse=True)[0]
        return links[qualities[str(quality)]]
    except:
        print(fallback_m3u)
        print('sleeping for 60 seconds...')
        time.sleep(60)
        return fallback_m3u

# Step 1: Load Twitch channels from your server
twitch_channels = s.get('https://api.m3use.projectmoose.xyz/channels-twitch').json()
total = len(twitch_channels)
print(f'{total} twitch channels found')

# Step 2: Iterate
for count, channel in enumerate(twitch_channels, 1):
    url = channel.get('url', '').strip().strip('/')
    m3u8_url = channel.get('m3u8-url', '').strip()
    streamer_id = url.split('/')[-1]

    print('sleeping for 5 seconds...')
    time.sleep(5)

    # Offline check
    try:
        html = s.get(url, timeout=5).text
        viewers = s.get(f'https://decapi.me/twitch/viewercount/{streamer_id}', timeout=5).text
    except:
        html, viewers = '', '0'

    if '"isLiveBroadcast":true' not in html and not viewers.isdigit():
        print(f'{count} : {url} : offline')
        channel['m3u8-url'] = fallback_m3u
        continue

    print(f'{count} : {url} : looks online')

    if is_valid_m3u8(m3u8_url):
        print(f'{count} : {url} : existing m3u8 is valid')
        continue

    print(f'{count} : {url} : fetching new m3u8')
    m3u8 = getm3u(url)

    if m3u8 == fallback_m3u:
        print(f'{count} : {url} : RETRYING...')
        m3u8 = getm3u(url)

    channel['m3u8-url'] = m3u8

# Step 3: Save
with open('twitch.json', 'w') as f:
    json.dump(twitch_channels, f, indent=4)
