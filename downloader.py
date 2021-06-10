from pytube import YouTube
from pytube import Playlist

def download():
    print("si vous souhaitez telecharger une video tapez 1, pour une musique 2 pour une playlist 3")
    choice= int(input())
    if choice == 1:
        print("entrez le lien s'il vous plait")
        link = input()
        yt = YouTube(link)
        #Title of video
        print("Title: ",yt.title)
        #Number of views of video
        print("Number of views: ",yt.views)
        #Length of the video
        print("Length of video: ",yt.length,"seconds")
        #Rating
        print("Ratings: ",yt.rating)
        #printing all the available streams
        print(yt.streams.filter(progressive=True))
        print("please choose your quality by entering the itag number")
        ys = yt.streams.get_by_itag(input())
        #Starting download
        print("telechargement en cours de {yt.title}")
        ys.download()
        print("telechargement fini")
    elif choice == 2 :
        print("entrez le lien s'il vous plait")
        link = input()
        yt=YouTube(link)
        t=yt.streams.filter(only_audio=True).all()
        t[0].download()
    elif choice == 3 : 
        print("pour une playlist de video tapez 1 pour une playlist d'audio tapez deux")
        choice2 == int(input())
        if choice2 == 1:
            print("please enter the link of your playlist")
            p = Playlist(input())
            i = 0
            for video in p.videos:
                i += 1
                print("video number ", i ,"is being downloaded is being downloaded")
                video.streams.first().download()
                print("video number" , i ," is downloaded")
            print("download done")
        elif choice2 == 2:
            print("please enter the link of your playlist")
            p = Playlist(input())
            i = 0
            for video in p.videos:
                i += 1
                print("video number ", i ,"is being downloaded is being downloaded")
                video.streams.filter(only_audio=True).first().download()
                print("video number" , i ," is downloaded")
            print("download done")
        else:
            download()
    else:
        print("error in input please try again")
        download()
download()