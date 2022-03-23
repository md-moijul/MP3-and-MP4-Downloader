from tkinter import *

root = Tk()
root.title("mp3/mp4 downloader")
root.geometry("400x400")

Status = Label(root, text ="Welcome to mp3/mp4 downloader!\nStart to download")
Status.grid(row=0, column=0)

link_text = Label(root, text="drop your link bellow to :")
link_text.grid(row=1, column= 0)
link_entry= Entry(root, width = 30)
link_entry.grid(row= 2, column = 0)
down_button = Button(root, text="Download")
down_button.grid(row= 3, column = 0)



root.mainloop()