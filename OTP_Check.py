import random
from tkinter import *
import tkinter.messagebox as msgbx
import json
import requests

root=Tk()
rand=random.randint(1111,9999)

message="Your OTP is {}".format(rand)

def send_sms(num,msg):
    url="https://www.fast2sms.com/dev/bulkV2"
    params={"authorization":"S63gbyre25wRO9JhVGEpFtDANxPLkdBMYoaIuZmcsz4C7i1Wfvavq7DeLy18cMFxbC2o43RGgJtYPjEs","sender_id":"TXTIND","message":msg, "route":"v3","numbers":num}
    headers={"cache-control":"no-cache"}
    res=requests.request("GET",url,headers=headers,params=params)
    print(res.text)
    
def send():
    Mob=Mobile_number.get()
    if Mob=='':
        msgbx.showinfo("Error","Mobile number is blank")
    elif len(Mob)!=10:
        msgbx.showinfo("Error","Incorrect Mobile Number")
    else:
        send_sms(Mob,message)

def Check_OTP():
    opt=OTP.get()
    if int(opt)==rand:
        msgbx.showinfo("success","OTP Verified")
    else:
        msgbx.showinfo("OOPS", "OTP is wrong, Try again")


root.geometry('500x500')
root.title("OTP_Checker")

Mobile_number=StringVar()
OTP=StringVar()



l1=Label(root,text="Mobile No:",font='Arial').place(x=40,y=60)
l2=Label(root,text="OTP:",font='Arial').place(x=40,y=100)
e1=Entry(root,width=30,textvariable=Mobile_number).place(x=120,y=60)
e2=Entry(root,width=30,textvariable=OTP).place(x=120,y=100)
b1=Button(root,width=10,text='Send OTP',command=send).place(x=40,y=140)
b2=Button(root,width=10,text='Submit OTP',command="Check_OTP").place(x=40,y=180)



root.mainloop()