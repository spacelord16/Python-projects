import pytube

url = "https://www.youtube.com/watch?v=AFEZzf9_EHk"

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'C:\Users\Aditya\Desktop\Youtube Download')
