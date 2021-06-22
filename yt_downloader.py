from tkinter import *
from pytube import YouTube
from os import *

root=Tk()
root.minsize(500,800)
root.title('Youtube Downloader')
Label(root,text="Hi.You can download any video here",font='Arial 15').pack()
link=StringVar()
enter_link=Entry(root, text='Enter your Link', width=70,textvariable=link).place(x=30,y=90)

url=YouTube(str(link.get()))
def downloader():# function for downloader
    url=YouTube(str(link.get()))
    video= url.streams.get_highest_resolution()
    video.download('C:\\Users\\Admin\\Desktop\\youtube_converter')
    Label(root,text='DOWNLOADED',font='Arial 10').place(x=190,y=210)
def opener():
    path='"C:\\Users\\Admin\\Desktop\\youtube_converter'
    name=url.title+'.mp4'
    startfile(os.path.join(path,name))# need to add a button to open the downloaded youtube file
    
Button(root,text='Download',font='Arial 10 bold', bg='violet',padx=2, command=downloader).place(x=180,y=150) #the command function here links the function to the button
Button(root,text='Open',font='Arial 10 bold', bg='violet',padx=2, command=opener).place(x=200,y=200)
root.mainloop()