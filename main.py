import tkinter as tk
from PIL import Image,ImageTk
import random

window = tk.Tk()
window.geometry("600x600")
window.title("Dice Roll Simulator")

dice = ["one.png", "Two.png", "Three.png", "Four.png", "Five.png", "Six.png"]
imagedice = ImageTk.PhotoImage(Image.open(random.choice(dice)))
labelImage = tk.Label(window, image=imagedice)
labelImage.image = imagedice
labelImage.place(x=40, y=50)
def dice_roll():
    imagedice = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    labelImage.configure(image=imagedice)
    labelImage.image = imagedice

button=tk.Button(window,text="Roll Dice",bg="Green",fg="White",command=dice_roll)
button.place(x=280,y=15)
window.mainloop()

