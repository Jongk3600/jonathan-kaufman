from tkinter import *

# Creates window
change_email_window = Tk()
change_email_window.title('Change Login Email')

def edit_login_email(email):
    """
    This function checks value for @
    and if it contains it adds value
    to the login_email.txt file.
    """
    if '@' not in email: # This if statement checks to see if value contains @
        invalid = Tk()
        invalid.title('Invalid Email')
        invalid_email_label = Label(invalid, text = 'Not a valid Email!')
        close_invlaid_window = Button(invalid, text = 'Close Window', command = invalid.destroy)
        invalid_email_label.grid(row = 1, column = 1)
        close_invlaid_window.grid(row = 2, column = 1)
    else:
        email_file = open('login_email.txt','w')
        email_file.write(email)
        email_file.close()
        info_recieved_window = Tk()
        info_recieved_window.title('Info Recieved')
        info_recieved_label = Label(info_recieved_window, text = 'New Login Email Recorded!')
        close_window = Button(info_recieved_window, text = 'Close Window', command = info_recieved_window.destroy)
        info_recieved_label.grid(row = 1, column = 1)
        close_window.grid(row=2, column=1)
        info_recieved_window.mainloop()

# Starts the main part of program
main_label = Label(change_email_window, text = 'Please enter in new login email!')
email_label = Label(change_email_window, text = 'Email:')
email_entry = Entry(change_email_window, width = 25)
submit_email = Button(change_email_window, text = 'Submit Email', command = lambda: edit_login_email(email_entry.get()))

main_label.grid(row = 1, columnspan = 5)
email_label.grid(row = 2, column = 1)
email_entry.grid(row = 2, column = 2)
submit_email.grid(row = 3, columnspan = 5)
change_email_window.mainloop()
