from tkinter import *
class GUI:
    def __init__(self):
        
        # similar to root in other texts
        window = Tk()
 
        name_label = Label(window, text='Enter Name:')
        name_label.pack(anchor="c")
        self.name_field = Entry(window)
        self.name_field.pack(anchor="c")

        button_label = Label(window, text='Press Button to Print')
        button = Button(window, text='Print', command=self.doPrint)

        button_label.pack()
        button.pack()

        #waiting for user input - event driven program
        window.mainloop()
        
    def doPrint():
        print(self.name_field.get())

#initialises the programme
GUI()
