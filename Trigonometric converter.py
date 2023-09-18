#simple_sinse,cos,tan converter
from tkinter import*
import math
window=Tk()
entry=Entry(window,font=('Bnazanin',20,'bold'),bg='white',bd=10)
entry.grid(row=1,column=0,columnspan=4)


    
def tan(int):
     entry.delete(0,'end')
     entry.insert(0,(math.tan(int)))

def get_key_t():
     try:
       in_num=float(entry.get())
       #print(in_num)#تا وقتی کامند را فعال نکنیم پرینت کار نمیکند
       tan(in_num)
     except:
         entry.delete(0,'end')
         entry.insert(0,("invalid input "))
     


def cos(inc):
        entry.delete(0,'end')
        entry.insert(0,(math.cos(inc)))

def get_key_c():
     
     try:
       in_num=float(entry.get())
       #print(in_num)#تا وقتی کامند را فعال نکنیم پرینت کار نمیکند
       cos(in_num)
     except:
         entry.delete(0,'end')
         entry.insert(0,("invalid input "))
    

def sinse(ins):
        entry.delete(0,'end')
        entry.insert(0,(math.sin(ins)))

def get_key_s():
     
     try:
       in_num=float(entry.get())
       #print(in_num)#تا وقتی کامند را فعال نکنیم پرینت کار نمیکند
       sinse(in_num)
     except:
         entry.delete(0,'end')
         entry.insert(0,("invalid input "))

def get_clear():
     entry.delete(0,'end')
         
       



#Buttons

""" sin """
but_dec=Button(window,font=('Bnazanin',20,'bold'),text='sin',command=get_key_s)
but_dec.grid(row=2,column=0,sticky=W,padx=10,pady=20)

""" cos """
but_bin=Button(window,font=('Bnazanin',20,'bold'),text='cos',command=get_key_c)
but_bin.grid(row=2,column=0,sticky=E,padx=100,pady=20)

"""tan"""
but_oct=Button(window,font=('Bnazanin',20,'bold'),text='tan',command=get_key_t)
but_oct.grid(row=2,column=1,sticky=E,padx=10,pady=20)

"""delete"""
but_hex=Button(window,font=('Bnazanin',20,'bold'),text='delet',command=get_clear)
but_hex.grid(row=2,column=1,sticky=W,padx=100,pady=20)

window.mainloop()