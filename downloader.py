from pytube import YouTube


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
print("telechargement en cours")
ys.download()
print("telechargement fini")