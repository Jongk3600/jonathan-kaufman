from tkinter import *
import datetime

def close_window(root):
    root.destroy()

def submit():
    with open('weather_data.doc','a+') as out_file:
        out_file.write('Date: '+date.get()+'\n')
        out_file.write('Condtions: '+conditions.get()+'\n')
        out_file.write('Prcipitation Type: '+tkvar.get()+'\n')
        out_file.write('High: '+high_temp.get()+'\n')
        out_file.write('Low: '+high_temp.get()+'\n')
        out_file.write('\n')
        out_file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        out_file.write('------------------------------\n')
        date.delete(0, 'end')
        conditions.delete(0, 'end')
        high_temp.delete(0, 'end')
        low_temp.delete(0, 'end')
        tkvar.set(' ')
    window_2= Tk()
    window_2.title('Record Recieved')
    submit_message= Label(window_2, text= 'Your submission has been recorded!')
    close= Button(window_2, text= 'Close Window', command= lambda: close_window(window_2))
    submit_message.grid(row= 1, column= 1)
    close.grid(row= 2, column= 1)

window= Tk()
window.title('Record Weather Data')
window.geometry('350x250')

precip_options= ['Rain','Snow','Sleet','Wintry Mix','None']
tkvar= StringVar(window)
tkvar.set(' ')

record_label= Label(window, text= 'Enter in Weather Data and press submit to log weather data!')
space= Label(window, text= '')
space_2= Label(window, text= '')

date_label= Label(window,text= 'Date (MM/DD/YYYY):')
date= Entry(window)

conditions_label= Label(window, text= 'Conditions:')
conditions= Entry(window)

high_temp_label= Label(window, text= 'High:')
high_temp= Entry(window)

low_temp_label= Label(window, text= 'Low:')
low_temp= Entry(window)

precip_type_label= Label(window, text= 'Precipitation Type:')
precip_type= OptionMenu(window,tkvar, *precip_options)

submit= Button(window, text= 'Submit', command= submit)

copyright_info= Label(window, text= '©2019 by Jonathan Kaufman. Version: 1.1')
copyright_line2= Label(window, text= 'ECWS has been granted rights to this program.')

record_label.grid(row= 0, columnspan= 2)
space.grid(row= 1, column= 0)
date_label.grid(row= 2, column= 0)
date.grid(row= 2, column= 1)
conditions_label.grid(row= 3, column= 0)
conditions.grid(row= 3, column= 1)
high_temp_label.grid(row= 4, column= 0)
high_temp.grid(row= 4, column= 1)
low_temp_label.grid(row= 5, column= 0)
low_temp.grid(row= 5, column= 1)
precip_type_label.grid(row= 6, column= 0)
precip_type.grid(row= 6, column= 1)
space_2.grid(row= 7, column= 0)
submit.grid(row= 8, columnspan= 2)
copyright_info.grid(row= 9, columnspan= 2)
copyright_line2.grid(row= 10, columnspan= 2)

window.mainloop()
