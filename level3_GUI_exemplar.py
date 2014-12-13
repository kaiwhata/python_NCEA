#-------------------------------------------------------------------------------
# Name:        List of schools
# Purpose:     List of schools using OOP and lists to capture school data,
#              create instance objects, store in list and write to CSV file
#              Enhanced to include get methods for class School.
#              Enhanced to incorporate a GUI to collect input.
#              Enhanced to include unique school name
#
# Authors:     Edwin Bruce (with edits from Elf Eldridge)
# Created:     13/12/2014
# Licence:     CC
# Version:     Tested in Python 3.4
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#import GUI library
from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox

class School:
    def __init__(self, school_name):
        self.school_name = school_name

    def get_school_name(self):
        return self.school_name

#create the GUI interface
class GUI:
    def __init__(self):

        # similar to root in other texts
        window = Tk()
        window.title("Data Entry for schools data")
        #setting root window and size
        window.minsize(width=200, height=200)

        #this will contain the list of all schools entered via the gui
        self.recordlist = []
        #this will allow us to only write to csv once our data has been validated
        self.ready_to_write= False

        #creating label and field variable in GUI for each entry field
        school_name_label = Label(window, text='Enter School Name:')
        school_name_label.pack(anchor="c") #.pack() places the component in the window
        self.school_name_field = Entry(window)
        self.school_name_field.pack(anchor="c")

        #creates a button. The command function is run when the button is pressed
        #the 'command=self.doSubmit' is an example of a callback method
        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='Write to csv', command=self.writetocsv)
        button_label.pack()
        button.pack()
        button_label1.pack()
        button1.pack()

        #waiting for user input - event driven program
        window.mainloop()


    def doSubmit(self):
        #test uniqueness of each school name entered
        noduplicate = True
        for record in self.recordlist:
            if self.school_name_field.get() == record.get_school_name():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate school name \n Please enter school name again')

        if noduplicate == True:
        #this is the callback method for the 'Submit' button
            if len(self.school_name_field.get()) <1:
                tkinter.messagebox.showwarning('Warning!','Please enter text value for School name')
            else:
                try:
                    self.recordlist.append(School(self.school_name_field.get()))
                    self.ready_to_write= True
                    tkinter.messagebox.showinfo('Notice','Submission Sucessful')
                    self.school_name_field.delete(0, END) #command to clear field

                except:
                    tkinter.messagebox.showwarning('Warning!','Please enter a different school name')


    def writetocsv(self):
        #this is the callback method for the 'write to csv' button
        import csv
        file_name = 'schools_database.txt'

        if self.ready_to_write: #checks data has been previously validated
            ofile = open(file_name, 'w') #open with write('w') or append('a') privelages
            writer = csv.writer(ofile, delimiter=',')
            #writes header row
            writer.writerow(['School Name'])
            #cycles through list of records created by gui
            for record in self.recordlist:
                writer.writerow([record.get_school_name()])
            #explicitly closes the output file
            ofile.close()
            tkinter.messagebox.showinfo('Notice', ('File %s Generated Sucessfully' % file_name))
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False
        
#initialises the programme
GUI()
