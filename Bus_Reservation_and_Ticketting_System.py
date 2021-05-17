
#By Coder_CHIBUZO (JOHN CHIBUZO IYIOKE)


import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox

import sqlite3
con=sqlite3.Connection('hrdb')




rootp=Tk()
rootp.title('My Transport Company Booking App')
rootp.geometry('600x300')
Label(rootp,text="My Transport Booking System",font="Bold 20").place(relx=0.1,rely=0.1)
rootp.iconify()


def cancel_reservation():
    rootp.destroy()
    root2=Tk()
    root2.title("Welcome,Customer To our Cancellation System")
    root2.geometry('600x300')
    Label(root2,text="Enter Phone Number").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1)
    Label(root2,text="Choose Vehicle Type").grid(row=1,column=0)
    w2=ttk.Combobox(root2,height=5,width=15,values=["Bus","Salon"])
    w2.grid(row=1,column=1)
    Label(root2,text="select boarding Termina").grid(row=2,column=0)
    w3=ttk.Combobox(root2,height=5,width=15,values=["Enugu","Lagos","Abuja","Kaduna","PortHarcourt","Delta","Kano",
            "Ibanda","Anambra","Imo","Bayelsa"])
    w3.grid(row=2,column=1)


    def CancelReservation():
        d=e1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        x=str(d)
        y=str(c)
        con.commit()
        if d=='' or b=='' or c=='':
             tkinter.messagebox.showerror("Oops!!","You can't leave any field empty")
        else:     
             if b=="bus":
                cur.execute("delete from BUS where adno=(?) and boarding=(?)",(d,b,))
                cur.execute("select * from BUS")
                tkinter.messagebox.showinfo("your reservation is cancelled",cur.fetchall())
             else:
                    cur.execute("delete from Salon where adno=x and boarding=y")
                    cur.execute("select * from Salon")
        
                    
            
    Button_CancelReservation=Button(root2,text="Cancel Reservation",command=CancelReservation).grid(row=4,column=0)
    root2.mainloop()

def search_trip():
    rootp.destroy()
    root4=Tk()
    root4.title("Search availblity")
    root4.geometry('600x300')
    Label(root4,text="Boarding Termina").grid(row=0,column=0)
    w1=ttk.Combobox(root4,height=5,width=15,values=["Enugu","Lagos","Abuja","Kaduna","PortHarcourt","Delta","Kano",
            "Ibanda","Anambra","Imo","Bayelsa"])
    w1.grid(row=0,column=1)
    Label(root4,text="Destination Termina").grid(row=1,column=0)
    w2=ttk.Combobox(root4,height=5,width=15,values=["Enugu","Lagos","Abuja","Kaduna","PortHarcourt","Delta","Kano",
            "Ibanda","Anambra","Imo","Bayelsa"])
    w2.grid(row=1,column=1)
    Label(root4,text="Choose day of travel").grid(row=2,column=0)
    w3=ttk.Combobox(root4,text="choose day",height=5,width=15,values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    w3.grid(row=2,column=1)
    def check_availibility():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        if a=='' or b=='' or c=='':
            tkinter.messagebox.showerror("Error","Cant leave any field empty")
           
                
        else:
             if a!=b:
                 #cur.execute("create table avableTrip(boarding char(20),destination char(20),day char(20),time number,class char(10),fare number)")
                 cur.execute("insert into avableTrip values('Enugu','Lagos','Sunday',8.00,'Bus',7000)")
                 cur.execute("insert into avableTrip values('Enugu','Abuja','Monday',7.00,'Bus',6500)")
                 cur.execute("insert into avableTrip values('Enugu','Kaduna','Tuesday',8.00,'Salon',7300)")
                 cur.execute("insert into avableTrip values('Enugu','PortHarcourt','Wensday',4.00,'Salon',3500)")
                 cur.execute("insert into avableTrip values('Enugu','Delta','Wensday',5.00,'Salon',5000)")
                 cur.execute("select * from avableTrip where boarding=? and destination=? and day=?",(a,b,c,))
                 con.commit()
                 e=cur.fetchall()
                 tkinter.messagebox.showinfo("Availble Trips", e)
             else:
                tkinter.messagebox.showerror("Oops","boarding and destination can't me same")
        
    Bs=Button(root4,text="Search Trip Availblity",command=check_availibility).grid(row=3,column=0)
    root4.mainloop()


def book_trip():
    rootp.destroy()
    root=Tk()
    root.title('Trip search And booking')
    root.geometry('600x300')
    label_BoardingLocation=Label(root,text="Boarding Termina").grid(row=1,column=0)
    #e1=Entry(root,width=20,bd=4,justify="right")
    #e1.grid(row=1,column=1)
    
    Boarding_Termina=ttk.Combobox(root,height=5,width=15,values=["Enugu","Lagos","Abuja","Kaduna","PortHarcourt","Delta","Kano",
            "Ibanda","Anambra","Imo","Bayelsa"])
    Boarding_Termina.grid(row=1,column=1)
    label_DestinationLocation=Label(root,text='Destination Termina').grid(row=2,column=0)
   
    
    Destination_Termina=ttk.Combobox(root,height=5,width=15,values=["Enugu","Lagos","Abuja","Kaduna","PortHarcourt","Delta","Kano",
            "Ibanda","Anambra","Imo","Bayelsa"])
    Destination_Termina.grid(row=2,column=1)
    
    label_PhoneNumber=Label(root,text='Enter Phone Number').grid(row=3,column=0)
    Phone_Number=Entry(root,width=20)
    Phone_Number.grid(row=3,column=1)
    Vehicle_Type=ttk.Combobox(root,text='Vehicle Type',height=5,width=15,values=["Bus","Salon"])
    Vehicle_Type.grid(row=4,column=1)
    label_VehicleType=Label(root,text='Vehicle Type').grid(row=4,column=0)
    label_TravelDate=Label(root,text="Travel Day").grid(row=5,column=0)
    Travel_Day=ttk.Combobox(root,text="choose day",height=5,width=15,values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    Travel_Day.grid(row=5,column=1)
    label_DepartureTime=Label(root,text="DepartureTime").grid(row=6,column=0)
    DepartureTime=ttk.Combobox(root,height=5,width=15,values=["7:00 AM","8:00 AM","10:00 PM"])
    DepartureTime.grid(row=6,column=1)

    def confirm_booking():
        a=Boarding_Termina.get()
        b=Destination_Termina.get()
        c=Phone_Number.get() 
        d=Vehicle_Type.get()
        f=Travel_Day.get()
        g=DepartureTime.get()
        x=(a,b,c,f,g)
        cur=con.cursor()
        
        if a=='' or b=='' or c=='' or d=='' or f=='' or g=='':
            tkinter.messagebox.showerror("OOPS","you can't leave any field empty")
        else :
            if d=='Bus':
                
                if a!=b:
                    #cur.execute(" to create table BUS(boarding char(20),destination char(20),adno number,day char,time number)")
                    cur.execute("insert into BUS values(?,?,?,?,?)",x)
                    tkinter.messagebox.showinfo("congrats","your seat has been reserved")
                    con.commit()
                    cur.execute("select * from BUS where adno=(?)",(c,))
                    tkinter.messagebox.showinfo("records",cur.fetchall())
                else:
                    tkinter.messagebox.showerror("Error","you can't choose same city")
            if d=='Salon':
                #cur.execute("to create table Salon(boarding char(20),destination char(20),adno number,day char,time number)")
                
                if a!=b:
                    cur.execute("insert into Salon values(?,?,?,?,?)",x)
                    tkinter.messagebox.showinfo("congrats","your seat has been reserved")
                    con.commit()
                    cur.execute("select * from Salon where adno=(?)",(c,))
                    tkinter.messagebox.showinfo("records",cur.fetchall())
                else :
                    tkinter.messagebox.showerror("Error","you can't choose same city")
    Bi=Button(root,text="CONFIRM BOOKING",bg='green',command=confirm_booking).grid(row=7,column=1)

    root.mainloop()
    
Button_Book=Button(rootp,text="BOOK A TRIP",command=book_trip).place(relx=0.25,rely=0.35)
#Button_Book=Button(rootp,text="BOOK A TRIP",command=lambda:book_trip()).place(relx=0.25,rely=0.35)

Button_Search=Button(rootp,text="SEARCH A TRP",command=search_trip).place(relx=0.5,rely=0.35)
#Button_Search=Button(rootp,text="SEARCH A TRP",command=lambda:search_trip()).place(relx=0.5,rely=0.35)

Button_Cancel=Button(rootp,text="CANCEL RESERVATION",command=cancel_reservation).place(relx=0.3,rely=0.5)
#Button_Cancel=Button(rootp,text="CANCEL RESERVATION",command=lambda:cancel_reservation()).place(relx=0.3,rely=0.5)


rootp.mainloop()
    
