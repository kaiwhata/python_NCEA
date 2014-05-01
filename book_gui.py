#import GUI library
from tkinter import *

#create the book class incorporating instance variables and methods
class Book:
    def __init__(self, title_i, author_i, isbn_i):
        self.title = title_i
        self.author= author_i
        self.isbn=isbn_i
        self.type= 'Book'
        self.is_read= False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_type(self):
        return self.type

    def get_isbn(self):
        return self.isbn

    def get_is_read(self):
        return self.is_read

    def read(self):
        self.is_read = True



#create the GUI interface
class GUI:

    def __init__(self):

        # similar to root in other texts
        window = Tk()
        window.title("Data Entry Screen")
        #setting root window and size
        window.minsize(width=400, height=200)

        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all books entered via the gui
        self.recordlist = []

        #creating label and field variable in GUI for each entry field
        name_label = Label(window, text='Enter Title:')
        name_label.pack() #.pack() places the component in the window
        self.name_field = Entry(window)
        self.name_field.pack()

        author_label = Label(window, text='Enter author:')
        author_label.pack()
        self.author_field = Entry(window)
        self.author_field.pack()

        isbn_label = Label(window, text='Enter isbn:')
        isbn_label.pack()
        self.isbn_field = Entry(window)
        self.isbn_field.pack()

        #creates a button. The command function is run when the button is pressed
        #the 'command=self.doSubmit' is an example of a callback method
        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='write to csv', command=self.writetocsv)
        button_label.pack()
        button.pack()
        button_label1.pack()
        button1.pack()

        #waiting for user input - event driven program
        window.mainloop()


    def doSubmit(self):
        #this is the callback method for the 'Submit' button
        if len(self.name_field.get()) <1 or len(self.author_field.get()) <1 or len(self.isbn_field.get()) <1:
            tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
        else:
            try:
                validated_isbn = int(self.isbn_field.get())
                self.recordlist.append(Book(self.name_field.get(),self.author_field.get(), self.isbn_field.get()))
                self.ready_to_write= True
                tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                self.author_field.delete(0, END) #command to clear field
                self.name_field.delete(0, END)
                self.isbn_field.delete(0, END)
            except:
                tkinter.messagebox.showwarning('Warning!','Please enter numeric isbn code')
                print('Please enter numeric isbn code')


    def writetocsv(self):
        #this is the callback method for the 'write to csv' button
        import csv
        file_name = 'database.txt'

        if self.ready_to_write: #cheacks data has been previously validated
            ofile = open(file_name, 'a') #open with write('w') or append('a') privelages
            writer = csv.writer(ofile, delimiter=',')
            #cycles through list of records created by gui
            for record in self.recordlist:
                print(record.get_title())
                writer.writerow([record.get_title(),record.get_author(), record.get_isbn(), record.get_is_read()])
            #explicitly closes the output file
            ofile.close()
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

#initialises the programme
GUI()
