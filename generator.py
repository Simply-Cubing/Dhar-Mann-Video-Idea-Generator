import random
from tkinter import *
from PIL import ImageTk, Image  
from topics import topics
from word1 import word1
from word2 import word2
from pt3 import pt3
from pt4 import pt4



root = Tk()
root.geometry("800x500")
root.title("dhar mann video idea generator")

generate_btn_img_original = PhotoImage(file=path)
generate_btn_img = generate_btn_img_original.subsample(3,3)

seed0 = random.randint(0,3)
seed1 = random.randint(0, 16)
seed2 = random.randint(0, 14)
seed3 = random.randint(0,4)
seed4 = random.randint(0, 3)
img_seed = random.randint(0, 10)

dhar_img = ImageTk.PhotoImage(Image.open(path))


#generates segments of the title
a = word1[seed1]
b = word2[seed2]
c = pt3[seed3]
d = pt4[seed4]

text = f"{a} {b} {c}{d}"

label = Label(text=text, font=('arial',20))
label.pack()
label1 = Label(width = 400, height = 300, image=dhar_img)
label1.pack()



def generate():

    seed0 = random.randint(0,3)
    seed1 = random.randint(0, 16)
    seed2 = random.randint(0, 14)
    seed3 = random.randint(0,4)
    seed4 = random.randint(0, 3)
    img_seed = random.randint(0, 10)

    global dhar_img 
    dhar_img = ImageTk.PhotoImage(Image.open(path))


    #generates segments of the title
    a = word1[seed1]
    b = word2[seed2]
    c = pt3[seed3]
    d = pt4[seed4]
    
    text = f"{a} {b} {c}{d}"
    label.config(text=text)
    label1.config(image=dhar_img)
    return text

generate_btn = Button(root,image= generate_btn_img,command=generate,width=500, height =200).pack(side=BOTTOM,padx=0,pady=0)
root.mainloop()
