from __future__ import unicode_literals
import youtube_dl
import youtube_dl.utils
import os
import certifi


class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join('/Users/yosuniiiii/', 'Downloads')
        self.song()

    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411',
            }],
            'extractaudio': True,
            'outtmpl': self.save_path + '/%(title)s.%(ext)s',
            'noplaylist': True
        }
        youtube_dl.utils.std_headers['Referer'] = "https://www.google.com/"
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])


if __name__ == '__main__':

    url = input(" 링크를 입력하세요 \n >> ")
    Download(url)
