from tkinter import *
from PIL import ImageTk,Image
from myimages import *

window = Tk()
window.title('USCG Aux Interest Form')
window.geometry('400x400')

window.iconbitmap(r'C:\Users\jkauf\Desktop\Code Files\Code Projects\official_form\aux_icon.ico')

def submit_interest(name_entry,email_entry,interest_entry):
    name.delete(0, END)
    email.delete(0, END)
    interests.delete(0, END)
    submit_window = Tk()
    submit_window.title('Submission Recieved')
    submit_window.geometry('200x80')
    submit_message = Label(submit_window,text='Your Submission has been Recieved!')
    close_window = Button(submit_window,text='Close Window',command= lambda: submit_window.destroy())
    submit_message.grid(row=1,columnspan=4)
    close_window.grid(row=2,columnspan=4)

    submit_window.mainloop()
    
    with open('interest_list.doc','a+') as out_file:
        out_file.write('Name: '+name_entry+'\n')
        out_file.write('E-mail: '+email_entry+'\n')
        out_file.write('Interests: '+interest_entry+'\n')
        out_file.write('----------------------------------------\n')

pic= imageString
render = PhotoImage(data=pic)

image_label= Label(window)
image_label.config(image=render)

message = Label(window,text=' Flotilla 61 Interest Form')
message.config(font=("Courier", 18))

space = Label(window,text='')

name_label = Label(window,text='Name: ')
name_label.config(font=("Courier", 18))
name = Entry(window,width='38')

email_label = Label(window,text='E-mail: ')
email_label.config(font=("Courier", 18))
email = Entry(window,width='38')

interest_label = Label(window,text='Interests: ')
interest_label.config(font=("Courier", 18))
interests = Entry(window,width='38')

submit = Button(window,text='Submit',command= lambda: submit_interest(name.get(),email.get(),interests.get()))
space2 = Label(window,text= '')
copyright_label = Label(window,text='   ©2019 by Jonathan Kaufman. Flotilla 054-06-01 has rights to use this')

image_label.grid(row=1,columnspan=4)
message.grid(row=2,columnspan=4)
space.grid(row=3,columnspan=4)
name_label.grid(row=4,column=1) 
name.grid(row=4,column=2)
email_label.grid(row=5,column=1) 
email.grid(row=5,column=2)
interest_label.grid(row=6,column=1) 
interests.grid(row=6,column=2)
submit.grid(row=7,columnspan=4)
space2.grid(row=8,column=1) 
copyright_label.grid(row=9,columnspan=4)

window.mainloop()
