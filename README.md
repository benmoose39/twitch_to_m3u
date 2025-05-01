## 📡 From Global Playlist to Personalized Streaming — Introducing [M3USe](https://m3use.projectmoose.xyz)

Hey folks — if you've used or followed this repo in the past, you might remember it started as an automated GitHub Actions workflow that created a public M3U playlist of livestreams. You could request channels, and I'd manually add them to the playlist for everyone.

But things have evolved.

### 🎉 Meet [M3USe](https://m3use.projectmoose.xyz) — A Web App for Custom Livestream Playlists

✅ Add livestreams from **YouTube**, **Twitch**, and **Dailymotion**  
✅ Build your **own playlist** — no more global list  
✅ Use with **any IPTV player** (VLC, Kodi, TiviMate, etc.)  
✅ Your playlist, your links, your rules

💡 No more waiting for manual updates or one-size-fits-all playlists. You just paste the channel URL, and the backend takes care of the rest.

---

> This is an indie passion project powered by the [Project Moose Discord](https://discord.gg/dmgYmAEdee) — and it’s live now.  
> 🚀 Try it out: [https://m3use.projectmoose.xyz](https://m3use.projectmoose.xyz)

Got ideas, feedback, or requests? Drop by the Discord or open a discussion here!

---

[![Live App](https://img.shields.io/badge/Live%20App-M3USe-green?style=flat-square)](https://m3use.projectmoose.xyz)


--------------------------- END (old content below) ---------------------------

# twitch_to_m3u
m3u links of twitch streams for localhost

### How to use
> Edit the `autorun` (`.sh` for linux, `.bat` for windows) file, and change `127.0.0.1` to the IP of the device that you want to be the local server (eg.: `192.168.1.5`).

> Save the file

> Run `autorun`

> Add streams into the file `streams.txt`

> If the server IP is `192.168.1.5`, find the playlist at `192.168.1.5:9001/playlist.m3u`. Add this to tivimate (or any player that supports m3u)

### Connect
Discord: https://discord.gg/dmgYmAEdee



Credits to `pwn.sh` and `Streamlink`.
