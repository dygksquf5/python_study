from __future__ import unicode_literals
import youtube_dl
# import youtube_dl.utils
import os
# you need to install about ffmpeg on Homebrew :)


class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.abspath('Downloads')
        self.song()

    def song(self):
        # youtube_dl.utils.std_headers['Referer'] = "https://www.youtube.com/"
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
            'noplaylist': True,
            'nocheckcertificate': True,  # ssl 문제가 떠서 ca 체크 안하게 하기.
        }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])


if __name__ == '__main__':

    url = input(" 링크를 입력하세요 \n >> ")
    Download(url)