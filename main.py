import clips
from tkinter import *


#CLIPS
clips_environment = clips.Environment()



#TKINTER
root = Tk()

root.title('Cant decide what to watch')

def answer_clicked(ans):
    pass

show_result = DISABLED

pytanie = Label(root, text='Movie or TV Show?')
answer1_button = Button(root, text='Movie', padx=100)
answer2_button = Button(root, text='TV Show', padx=100)


pytanie.grid(row=0, column=1)
answer1_button.grid(row=1, column=0)
answer2_button.grid(row=1, column=2)


#canvas = tkinter.Canvas(root, width=1280, height=720)

root.mainloop()
