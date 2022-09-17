import youtube_dl

ydl_opt = {
    #'listformats': True , 
    'format' : '18',
    'outtmpl': '%(title)s %(resolution)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=SD0s54grXCE"])
