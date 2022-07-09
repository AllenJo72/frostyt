from os import link
from pytube import YouTube
import sys 
from datetime import date

filedate = date.today()
link = str(sys.argv)
ytd = YouTube(link)
#seconds = ytd.lenght
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
print("Number of views: ",ytd.views)
print("Length of video: ",convert(ytd.length))
print("Rating of video: ",ytd.rating)
print(input("Click Enter to confirm download:"))
dwn = ytd.streams.get_highest_resolution()
dwn.download(f'downloads/{filedate}/')
