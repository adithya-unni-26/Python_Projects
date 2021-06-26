#importing the necessary modules 
import tkinter as tk
import datetime
from playsound import playsound 
from tkinter.messagebox import showinfo
import time


def alarm_time(time_two):
    #create date and time objects
    while True:
        time.sleep(1)
        time_set=datetime.datetime.now()
        time_disp=time_set.strftime("%H:%M")
        date=time_set.strftime("%D/%m/%Y")
        print(time_disp)
        if time_disp==time_two:
            playsound('/home/adi/projects/TF026.WAV')
            showinfo("YEEHAW", "Time To Wake up")
            break

def alarm_get():
    time_two=f'{hour.get()}:{minutes.get()}'
    alarm_time(time_two)


root=tk.Tk()
root.title('Alarm Gui')

hour=tk.StringVar()
minutes=tk.StringVar()

alarm_label= tk.Label(root,text="SET YOUR ALARM",font=('Arial',20,'bold')).grid(row=0,column=0,pady=10)
set_label= tk.Label(root,text='Enter Time').grid(row=2, column=0)
hour_entry= tk.Entry(root,textvariable=hour,width=10).grid(row=2,column=1)
min_entry=tk.Entry(root,textvariable=minutes,width=10).grid(row=2,column=2)
alarm_but=tk.Button(root,text='SET',command=alarm_get,width=15).grid(row=4,column=2,columnspan=2,pady=10)

root.mainloop()