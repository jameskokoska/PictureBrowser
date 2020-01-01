import glob
import time
import os
import tkinter
import tkinter.ttk as ttk
from PIL import ImageTk, Image

global totalFiles
totalFiles =(glob.glob("*.jpg"))
totalFiles +=(glob.glob("*.png"))
totalFiles.sort(key=os.path.getmtime)

favList = []
for file in totalFiles:
    if file[:11] == "Favourite -":
        favList.append(file)
favList.sort()

alreadyFav = -1
if favList != []:
    alreadyFav = int(favList[-1][12:-4])


window = tkinter.Tk()
window.configure(background="#cecbab")
window.minsize(width=1024, height=576)
window.title("Favourite Pics")

global index
index = -1
global favTotal
favTotal = 0

window.state('zoomed')
    
def startSearch():
    btnStart.destroy()
    startInfo.destroy()
    global index
    global totalFiles
    global image
    index += 1

    image = Image.open(totalFiles[index])
    n=0.25
    same = True
    [imageSizeWidth, imageSizeHeight] = image.size
    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    deathwing=Image.open(totalFiles[index])
    
    image2=deathwing.resize((newImageSizeWidth, newImageSizeHeight),Image.ANTIALIAS)
    Deathwing2=ImageTk.PhotoImage(image2)
    image = tkinter.Label(window, image = Deathwing2)
    image.pack(side = "bottom", fill="both", expand = "yes")
    window.mainloop()

def nextKey(event):
    global image
    image.destroy()
    global index
    global totalFiles
    index += 1
    if index == len(totalFiles):
        finished()
    else:
        img = ImageTk.PhotoImage(Image.open(totalFiles[index]))
        image = tkinter.Label(window, image = img)
        image.pack(side = "bottom", fill="both", expand = "yes")
        window.mainloop()

def prevKey(event):
    global image
    image.destroy()
    global index
    global totalFiles
    index -= 1
    img = ImageTk.PhotoImage(Image.open(totalFiles[index]))
    image = tkinter.Label(window, image = img)
    image.pack(side = "bottom", fill="both", expand = "yes")
    window.mainloop()

def fav(event):
    global index
    global totalFiles
    global favTotal
    favTotal += 1
    os.rename(totalFiles[index], "Favourite - " + str(alreadyFav+favTotal) + totalFiles[index][-4:])
    del totalFiles[index]

    global image
    image.destroy()
    if index == len(totalFiles):
        finished()
    else:
        img = ImageTk.PhotoImage(Image.open(totalFiles[index]))
        image = tkinter.Label(window, image = img)
        image.pack(side = "bottom", fill="both", expand = "yes")
        window.mainloop()

def finished():
    endInfo = tkinter.Text(window, height=15, width=100, font=("Helvetica",13), fg="white", bg="black")
    endInfo.pack()
    global favTotal
    endInfo.insert("1.0", str(favTotal) + " Files Favourited.")
    endInfo.insert("1.0", str("Finished all files in directory.\n"))
    

btnStart = tkinter.Button(window, text="Start Search", command=startSearch, height=5,
      width = 20,cursor = "circle", fg="blue")
btnStart.pack()

startInfo = tkinter.Text(window, height=15, width=100, font=("Helvetica",13), fg="white", bg="black")
startInfo.pack()
if favList != []:
    startInfo.insert("1.0", str("Found " + str(favList[-1][12:-4]) + " already favourited files.\n"))
startInfo.insert("1.0", str("Found " + str(len(totalFiles)) + " JPG and PNG files.\n"))
startInfo.insert("1.0", str("\n"))
startInfo.insert("1.0", str("The file will be renamed to Favourite - <index>.\n"))
startInfo.insert("1.0", str("To favourite a picture press <enter>.\n"))
startInfo.insert("1.0", str("Use the arrow keys <left> and <right> to scroll through the pictures.\n"))
startInfo.insert("1.0", str("Place the python file in the folder with the pictures, run the program.\n"))
startInfo.insert("1.0", str("To use this application:\n"))
startInfo.insert("1.0", str("Must be used on Windows, Made in Python 3.6.1, works with JPG and PNG files.\n"))
startInfo.insert("1.0", str("This application will help you sort through the pictures.\n"))


window.bind('<Return>', fav)
window.bind('<Right>', nextKey)
window.bind('<Left>', prevKey)
window.mainloop()
