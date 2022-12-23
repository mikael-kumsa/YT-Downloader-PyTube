from pytube import YouTube

def Download(link):
    youtubeOject = YouTube(link)
    youtubeOject = youtubeOject.streams.get_highest_resolution()
    x = youtubeOject.on_progress("")
    try:
        youtubeOject.download()
    except:
        print("There has been some error!")
    print("Download completed successfully!")

link = input("Enter the youtube url to be downloaded. URL: ")
Download(link)