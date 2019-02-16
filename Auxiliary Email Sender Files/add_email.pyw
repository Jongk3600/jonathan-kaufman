from tkinter import *

# Creates the window for main part of program
add_email_window = Tk()
add_email_window.title('Add Email')

def add_emails(email_1,email_2,email_3,email_4,email_5):
    """
    This is initiated by the press of the add emails button.
    This function appends the entered emails into the emails.txt
    file as well as displays a window that says the emails have
    been added.
    """
    with open('emails.txt','a') as email_file:
        if email_1 != '':
            email_file.write('\n'+email_1)
            email_1_entry.delete(0,'end')
        if email_2 != '':
            email_file.write('\n'+email_2)
            email_2_entry.delete(0, 'end')
        if email_3 != '':
            email_file.write('\n'+email_3)
            email_3_entry.delete(0, 'end')
        if email_4 != '':
            email_file.write('\n'+email_4)
            email_4_entry.delete(0, 'end')
        if email_5 != '':
            email_file.write('\n'+email_5)
            email_5_entry.delete(0, 'end')

    subbmitted_window = Tk()
    subbmitted_window.title('Emails Added')
    info_label = Label(subbmitted_window,text = 'Emails have been added!')
    close_window = Button(subbmitted_window,text = 'Close Window',command = subbmitted_window.destroy)

    info_label.grid(row = 1, column = 1)
    close_window.grid(row = 2,column = 1)

    subbmitted_window.mainloop()

# This starts main part of program
window_head = Label(add_email_window,text = 'Please enter the email(s) you want to add')

email_1_label = Label(add_email_window,text = 'E-mail 1:')
email_1_entry = Entry(add_email_window, width = 30)
email_2_label = Label(add_email_window,text = 'E-mail 2:')
email_2_entry = Entry(add_email_window, width = 30)
email_3_label = Label(add_email_window,text = 'E-mail 3:')
email_3_entry = Entry(add_email_window, width = 30)
email_4_label = Label(add_email_window,text = 'E-mail 4:')
email_4_entry = Entry(add_email_window, width = 30)
email_5_label = Label(add_email_window,text = 'E-mail 5:')
email_5_entry = Entry(add_email_window, width = 30)

add_email_button = Button(add_email_window,text = 'Add E-mails',command = lambda: add_emails(email_1_entry.get(),email_2_entry.get(),email_3_entry.get(),email_4_entry.get(),email_5_entry.get()))

window_head.grid(row = 1, columnspan = 5)
email_1_label.grid(row = 2, column = 1)
email_1_entry.grid(row = 2, column = 2)
email_2_label.grid(row = 3, column = 1)
email_2_entry.grid(row = 3, column = 2)
email_3_label.grid(row = 4, column = 1)
email_3_entry.grid(row = 4, column = 2)
email_4_label.grid(row = 5, column = 1)
email_4_entry.grid(row = 5, column = 2)
email_5_label.grid(row = 6, column = 1)
email_5_entry.grid(row = 6, column = 2)
add_email_button.grid(row = 7, columnspan = 5)

add_email_window.mainloop()
