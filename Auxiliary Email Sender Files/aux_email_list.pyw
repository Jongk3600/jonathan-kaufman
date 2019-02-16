from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


window= Tk()
window.title('Login')
window.geometry('200x120')

def send_email(subject,body,password):
    file = open('login_email.txt','r')
    file_read = file.readlines()
    open_emails = open('emails.txt')
    read_emails = open_emails.readlines()
    emails = ';'.join(read_emails)
    emails = emails.replace('\n','')
    fromaddr = str(file_read[0])
    toaddr = emails

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
 
    body_text = body
    msg.attach(MIMEText(body_text, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr.split(';'), text)
    server.quit()
    file.close()

def add_emails_to_list():
    import add_email

def run_change_email():
    import change_from_email


def compose_email():
    login_info = open('login_email.txt','r')
    readfile = login_info.readlines()
    server_password= password.get()
    print
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(readfile[0]), server_password)
        server.quit()
    except:
        invalid_window = Tk()
        invalid_window.title('Invalid Login')
        invalid_label = Label(invalid_window, text = 'Invalid Login!')
        invalid_label.grid(row = 1, column = 1)
        invalid_window.mainloop()
    password.delete(0,'end')
    window.destroy()
    compose_window = Tk()
    compose_window.title('Compose Email')
    compose_window.geometry('400x400')

    compose_label = Label(compose_window,text = 'Enter Email Message Below!')
    space_1 = Label(compose_window,text = '')
    subject_label = Label(compose_window,text = 'Subject: ')
    enter_subject = Entry(compose_window,width = 40)
    body_label = Label(compose_window,text = 'Body: ')
    enter_body = Text(compose_window,height = 15, width = 40)
    enter_body.insert(END,'\n\nFrom,\nJonathan Kaufman\nBQ, USCG Auxilairy Flotilla 054-06-01')
    space_2 = Label(compose_window,text = '')
    send_email_button = Button(compose_window,text = 'Send Email',command= lambda: send_email(enter_subject.get(),enter_body.get('1.0','end'),server_password))
    add_email_button = Button(compose_window,text = 'Add Emails',command = add_emails_to_list)


    compose_label.grid(row=1,columnspan=4)
    space_1.grid(row=2,columnspan=4)
    subject_label.grid(row=3,column=1)
    enter_subject.grid(row=3,column=2)
    body_label.grid(row=4,column=1)
    enter_body.grid(row=4,column=2)
    space_2.grid(row=5,columnspan=4)
    send_email_button.grid(row=6,columnspan=4)
    add_email_button.grid(row=7, column = 1)

    compose_window.mainloop()
                                                                                              
    

title = Label(window,text = 'Enter password to send e-mail')
space= Label(window,text = '')
password_label= Label(window,text = 'Password: ')
password= Entry(window,show= '*')
login_button= Button(window,text = 'Login', command= compose_email)
change_email_button = Button(window, text = 'Change Login Email', command = run_change_email)

title.grid(row=1,columnspan=4)
space.grid(row=2,columnspan=4)
password_label.grid(row=3,column=1)
password.grid(row=3,column=2)
login_button.grid(row=4,columnspan=4)
change_email_button.grid(row = 5, columnspan = 5)


window.mainloop()
