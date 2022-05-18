#importing files
import youtube_dl

video_url = input("please enter youtube video url:")

#call function from youtube_dl to extract file info(like video name)
video_info = youtube_dl.YoutubeDL().extract_info(
    url = video_url,download=False
)

#name the file after download
filename = f"Python/OutPutFiles/{video_info['title']}.mp3"

#download settings
options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filename,
}

#with this settings download file
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video_info['webpage_url']])
print("Download complete... {}".format(filename))
