import builtins
from tkinter import Entry,Button,Label,Tk,Text,StringVar
from pytube import YouTube

ventana=Tk()
ventana.title('descargas youtube')

def descarga():
    url=urlVideo.get()
    yt = YouTube(url).streams.get_by_itag(22).download()
    print('Descarga completada')
    ventana.destroy()

Label(ventana,text='descarga de python' , fg='gray' , font=('poppins' , 12)).grid (row=0 , column=0 , sticky='w' , padx=5 ,pady= 10)


urlVideo=StringVar()
urlEntry=Entry(ventana , textvariable=urlVideo, width=80 , font=('poppins' , 12))
urlEntry.grid(row=1,column=0,padx=20,pady=1,sticky='nsew')

botonDescarga=Button(ventana,text='Descarga',fg='black',font=('poppins' , 12) ,command=descarga)
botonDescarga.grid(row=2,column=0,padx=20,pady=20)

ventana.mainloop()
