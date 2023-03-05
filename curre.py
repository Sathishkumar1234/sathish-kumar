#importing tikinter it is using to creating [GUI]
import tkinter as tk
from tkinter import *
from tkinter import ttk 
from datetime import datetime
import requests
from tkinter import messagebox
from PIL import ImageTk,Image
import urllib.request
import shutil

#program exicution start
#CREATING WORK SPACE ITS USING tk.TK                                                    
#program exicution start
root=tk.Tk()
root.geometry("800x350")
root.title("currency converter")
root.maxsize(1000,370)
root.minsize(600,270)

#Create imgage url variable 
url = "https://xp.io/storage/ADnRjfM.jpg"
#Request to open the url using request and urllib module and store it  
res = urllib.request.urlopen(url)

#open the image and store it img
img = Image.open(res)
#set the image size using resize
resized = img.resize((300,150),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)

def show_data():
    amount=E1.get()
    from_currency=c1.get()
    to_currency=c2.get()
    #its importing API currency converting in official web site
    url='http://api.currencylayer.com/live?access_key=46091b14c71bb5e96ea28424b1e32e08'
    if amount == ' ':
        messagebox.showerror("Currency converter","please fill the amount")
    elif to_currency =='':
             messagebox.showerror("Currency converter","Please choose the currency")
    
    else:
        data=requests.get(url).json()
        #using the strip fuction is cleaning the json formate data(URL)(removeing (.),string spaces)
        currency=from_currency.strip()+to_currency.strip()
        amount=int(amount)
        cc=data['quotes'][currency]
        cur_conv=cc*amount
        E2.insert(0,cur_conv)
        text.insert('end',f'{amount} United State Dollar Equals = {cur_conv} \n\nLast time update\n{datetime.now()}')
        text.image_create("current",image = photo,padx=350,pady=30)
        
def clear():
    E1.delete(0,"end")
    E2.delete(0,'end')
    text.delete(1.0,'end')
l1=Label(root,text="USD CURRENCY CONVERSION",font=('roboto','12','bold'))
l1.place(x=200,y=8)
amt=Label(root,text='Amount',font=('roboto',11,'bold'))
amt.place(x=20,y=10)
E1=Entry(root,width=20,borderwidth=2,font=('roboto',11,'bold'))
E1.place(x=20,y=40)

c1=tk.StringVar()
c2=tk.StringVar()
currencychoose1=ttk.Combobox(root,width=25,textvariable=c1,state='readonly',font=('roboto',11,'bold'))
#adding comobo drop own list
currencychoose1['values']=['USD']
currencychoose1.place(x=300,y=40)
currencychoose1.current(0)

E2=Entry(root,width=20,borderwidth=1,font=('roboto',11,'bold'))
E2.place(x=20,y=80)

currencychoose2=ttk.Combobox(root,width=25,textvariable=c2,state='readonly',font=('roboto',11,'bold'))
currencychoose2['values']=('ALL',
                           'AFN ',
                           'ARS ',
                           'AWG',
                           'AUD',
                           'AZN',
                           'BSD',
                           'BBD',
                           'BYN',
                           'BZD',
                           'BMD',
                           'BOB',
                           'BAM',
                           'BWP',
                           'BGN',
                           'BND',
                           'KHR',
                           'CAD',
                           'KYD',
                           'CLP',
                           'CNY',
                           'COP',
                           'CRC',
                           'HRK',
                           'CUP',
                           'CZK',
                           'DKK',
                           'DOP',
                           'XCD',
                           'EGP',
                           'SVC',
                           'EUR',
                           'FKP',
                           'FJD',
                           'GHS',
                           'GIP',
                           'GTQ',
                           'GGP',
                           'GYD',
                           'HNL',
                           'HKD',
                           'HUF',
                           'ISK',
                           'INR',
                           'IDR',
                           'IRR',
                           'IMP',
                           'ILS',
                           'JMD',
                           'JPY',
                           'KZT',
                           'KPW',
                           'KRW',
                           'KGS',
                           'LAK',
                           'LBP',
                           'LRD',
                           'MKD',
                           'MYR',
                           'MUR',
                           'MXN',
                           'MNT',
                           'MZN',
                           'NAD',
                           'NPR',
                           'ANG',
                           'NZD',
                           'NIO',
                           'NGN',
                           'NOK',
                           'OMR',
                           'PKR',
                           'PAB',
                           'PYG',
                           'PEN',
                           'PHP',
                           'PLN',
                           'QAR',
                           'RON',
                           'RUB',
                           'SHP',
                           'SAR',
                           'RSD',
                           'SCR',
                           'SGD',
                           'SBD',
                           'SOS',
                           'ZAR',
                           'LKR',
                           'SEK',
                           'CHF',
                           'SRD',
                           'SYP',
                           'TWD',
                           'THD',                                                      
                           'TTD',
                           'TRY',
                           'TVD',
                           'UAH',
                           'GPA',
                           'UYU',
                           'UZS',
                           'VEF',
                           'VND',
                           'YER',
                           'ZWD')
currencychoose2.place(x=300,y=90)
currencychoose2.current()
text=Text(root,height=15,width=75,font=('verdana','9','bold'))
text.place(x=100,y=120)
B=Button(root,text='Search',bg='green',command=show_data,font=('verdana','10','bold',))
B.place(x=20,y=120)
clear=Button(root,text='Clear',bg='red',command=clear,font=('verdana','10','bold'))
clear.place(x=20,y=170)
root.mainloop()