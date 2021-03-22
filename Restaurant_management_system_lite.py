from tkinter import *
from tkinter import ttk
import datetime as calender
from tkinter import messagebox
import matplotlib.pyplot as plt

root=Tk()
root.config(bg='wheat1')

data1=StringVar()
data2=StringVar()
data3=StringVar()
data4=StringVar()
data5=StringVar()
data6=StringVar()
data7=StringVar()


current_date=calender.date.today()
data4.set(current_date)
total_list=[]
grand_total=0


dishes = ["French Fries", "Burger", "Pizza", "Coffee", "Sandwich", "Noodles", "Rice", "Soup", "Curry", "Hot Dog"]

quantity=[55,12,5,20,4,7,10,25,13,12]

def text_insert():
    """This method inserts the default data into the bill area."""

    text1.insert(END, '   Programmer Foundation Restaurant')
    text1.insert(END, '\n      Mountain view, California')
    text1.insert(END, '\n        contact:- 1234567890')
    text1.insert(END, '\n'
                          
                          '=====================================')
                          
def all_exit():
    wish1 = messagebox.askyesno("Confirm", "Do you want to exit?")
    if wish1 > 0:
        if data1.get() != '' or data2.get() != '' or data3.get() != '':
            wish2 = messagebox.askyesno("Confirm", "Would you like to save the data before exiting?")
            if wish2 > 0:
                return
            else:
                root.destroy()
        else:
            root.destroy()
    else:
        return

def value_generate():
    """This functions generates the bill of the customer"""

    ph_no = len(data3.get())
    if data1.get() == '' or data2.get() == '' or ph_no != 10:
        messagebox.showerror("Error!", "Please enter all the fields correctly.")
    else:
        text1.insert(END, f'Bill Number:-{data1.get()}')
        text1.insert(END, f'\nCustomer Name:- {data2.get()}')
        text1.insert(END, f'\nCustomer Contact:- {data3.get()}')
        text1.insert(END, f'\nDate:- {data4.get()}')
        text1.insert(END, '\n'
                              '========'
                              '=============================')

        text1.insert(END, 'ProductName  Quantity  percost  Total')

        text1.insert(END, '\n'
                              '=====================================')

def value_clear():
    """This method deletes all the data from the entry boxes"""

    data1.set('')
    data2.set('')
    data3.set('')
    data4.set('')
    data5.set('')
    data6.set('')
    data7.set('')
    
def value_reset():
    """This function resets the bill area"""

    text1.delete('1.0', END)
    text_insert()
    

def value_add():
    """This method adds up the order and shows in the bill area in the format of a table"""

    if data6.get() == '' or data7.get() == '':
        messagebox.showerror("Error", "Please enter all the details.")
    else:
        no_qtn = int(data6.get())
        no_cost = int(data7.get())
        total_cost = no_qtn * no_cost
        total_list.append(total_cost)
        text1.insert(END,
                         f'\n{data5.get()}\t       {data6.get()}\t        {data7.get()}     {total_cost}')


def value_total():
    """This function makes a total of all the order"""

    global grand_total
    for items in total_list:
        grand_total += items
    text1.insert(END, '\n'
                         
                          '=====================================')
    text1.insert(END, f'\t\t    Grand Total:- {grand_total}')
    text1.insert(END, '\n'
                          
                          '=====================================')

def plot():
	plt.pie(quantity,labels=dishes)
	plt.show()
	
style=ttk.Style()
style.configure("W.TButton",font=('calibri',8), background="black",borderwidth=4,relief="flat")

main_label=Label(root,text='Restaurant Management System',font=('ariel',10,'bold'),bd=8,bg='light gray',relief=GROOVE)
main_label.pack(side=TOP,fill=X)

frame1=Frame(root,bd=5,relief=GROOVE)
frame1.place(x=40,y=90,width=650,height=830)


frame2=Frame(root,bd=5,relief=GROOVE)
frame2.place(x=40,y=930,width=650,height=450)

frame3=Frame(frame1,bd=5,relief=GROOVE)
frame3.place(x=20,y=400,width=600,height=310)


frame4=Frame(root,bd=5,relief=GROOVE)
frame4.place(x=65,y=820,width=600,height=70)

label1=Label(frame1,text="Bill number")
label1.grid(row=0,column=0,sticky=W)

label2=Label(frame1,text="Customer Name")
label2.grid(row=1,column=0,sticky=W)

label3=Label(frame1,text="Customer contact")
label3.grid(row=2,column=0,sticky=W)

label4=Label(frame1,text="Date")
label4.grid(row=3,column=0,sticky=W)

label5=Label(frame1,text="Item purchased")
label5.grid(row=4,column=0,sticky=W)

label6=Label(frame1,text="Item quantity")
label6.grid(row=5,column=0,sticky=W)

label7=Label(frame1,text="Per cost")
label7.grid(row=6,column=0,sticky=W)

entry1=Entry(frame1,bd=5,textvar=data1,bg='antiquewhite1')
entry1.grid(row=0,column=1)

entry2=Entry(frame1,bd=5,textvar=data2,bg='antiquewhite1')
entry2.grid(row=1,column=1)

entry5=ttk.Combobox(frame1,width=19,textvar=data5,values=dishes)
entry5.grid(row=4,column=1)

entry4=Entry(frame1,bd=5,textvar=data4,bg='antiquewhite1')
entry4.grid(row=3,column=1)

entry3=Entry(frame1,bd=5,textvar=data3,bg='antiquewhite1')
entry3.grid(row=2,column=1)


entry1=Entry(frame1,bd=5,textvar=data6,bg='antiquewhite1')
entry1.grid(row=5,column=1)


entry1=Entry(frame1,bd=5,textvar=data7,bg='antiquewhite1')
entry1.grid(row=6,column=1)


button1=Button(frame3,text="Add",height=2,bd=3,width=6,bg='bisque2',command=value_add)
button1.grid(row=0,column=0,padx=4,pady=2)

button2=Button(frame3,text="Generate",height=2,bd=3,width=6,bg='bisque2',command=value_generate)
button2.grid(row=0,column=1,padx=4,pady=2)

button3=Button(frame3,text="Clear",height=2,bd=3,width=6,bg='bisque2',command=value_clear)
button3.grid(row=0,column=2,padx=4,pady=2)

button4=Button(frame3,text="Reset",height=2,bd=3,width=6,bg='bisque2', command=value_reset)
button4.grid(row=1,column=0,padx=4,pady=2)

button5=Button(frame3,text="Total",height=2,bd=3,width=6,bg='bisque2',command=value_total)
button5.grid(row=1,column=1,padx=4,pady=2)

button6=Button(frame3,text="Save",height=2,bd=3,width=6,bg='bisque2')
button6.grid(row=1,column=2,padx=4,pady=2)

button7=Button(frame3,text="Exit",height=1,bd=3,width=28,bg='bisque2',command=all_exit)
button7.grid(row=2,column=0,padx=4,pady=2,columnspan=3)

button8=ttk.Button(frame4,text="Graph",style="W.TButton",command=plot)
button8.grid(row=0,column=0,padx=4,pady=1)

button9=ttk.Button(frame4,text="Graph",style="W.TButton",command=plot)
button9.grid(row=0,column=1,padx=4,pady=1)

button10=ttk.Button(frame4,text="Graph",style="W.TButton",command=plot)
button10.grid(row=0,column=2,padx=4,pady=1)

text1=Text(frame2,bg='white')
text1.pack(fill=BOTH, expand=TRUE)

text_insert()

root.mainloop()