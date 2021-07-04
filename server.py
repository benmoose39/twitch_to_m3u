from flask import Flask, request
import requests
import sys

HOST = sys.argv[1]
PORT = 9001

app = Flask(__name__)

@app.route(f'/playlist.m3u')
def playlistgenerator():
    playlist = '#EXTM3U\n'
    with open('streams.txt', 'r') as streams:
        for stream in streams:
            stream = stream.strip()
            if not stream:
                continue
            playlist += f'#EXTINF:-1, {stream}\n'
            playlist += f'http://{HOST}:{PORT}/twitch?streamer={stream}\n'

    return playlist


@app.route(f'/twitch')
def getm3u():
    streamer = request.args.get('streamer')
    url = 'https://pwn.sh/tools/streamapi.py?url=twitch.tv/'
    try:
        response = requests.get(f'{url}{streamer}').json()
        links = response['urls']
        qualities = {int(key.replace('p','')) : key for key in links.keys() if key != 'audio_only'}

        m3u = ''
        for quality in sorted(qualities.keys(), reverse=True):
            m3u = m3u + links[qualities[quality]] + '\n'
                
    except:
        m3u = 'https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u'
    
    return f'#EXTM3U\n#EXT-X-INDEPENDENT-SEGMENTS\n#EXT-X-STREAM-INF:BANDWIDTH=290288\n{m3u}'

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

