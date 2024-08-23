from tkinter import *

first_number=second_number=operators=None

def get_digit(digit):
    current=str(result_label['text'])
    new = current + str(digit)
    result_label.config(text=new)

def clear():
       result_label.config(text='')

def get_operators(op):
    global first_number,operators
    first_number = int(result_label.cget('text'))

    #first_number=int(result_label.config['text'])
    operators=op
    result_label.config(text='')
    
def get_result():
    global first_number,second_number,operators
    second_number= int(result_label['text'])
    if operators == '+':
         result_label.config(text=str(first_number + second_number))
    elif operators == '-':
         result_label.config(text=str(first_number - second_number))
    elif operators == '*':
         result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config('Error')

        else:
            result_label.config(text=str(first_number / second_number))
        
    

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

result_label = Label(root,text='',bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=7,sticky='w',pady=(50,25))
result_label.configure(font=('verdana',30,'bold'))

butn7= Button(root,text=7,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(7))
butn7.grid(row=1,column=0)
butn7.configure(font=('verdana',14))

butn8= Button(root,text=8,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(8))
butn8.grid(row=1,column=1)
butn8.configure(font=('verdana',14))


butn9= Button(root,text=9,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(9))
butn9.grid(row=1,column=2)
butn9.configure(font=('verdana',14))

butn_add= Button(root,text='+',bg="green",fg="white",height=2,width=5,command=lambda: get_operators('+'))
butn_add.grid(row=1,column=3)
butn_add.configure(font=('verdana',14))

butn4= Button(root,text=4,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(4))
butn4.grid(row=2,column=0)
butn4.configure(font=('verdana',14))


butn5= Button(root,text=5,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(5))
butn5.grid(row=2,column=1)
butn5.configure(font=('verdana',14))


butn6= Button(root,text=6,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(6))
butn6.grid(row=2,column=2)
butn6.configure(font=('verdana',14))

butn_sub= Button(root,text='-',bg="green",fg="white",height=2,width=5,command=lambda: get_operators('-'))
butn_sub.grid(row=2,column=3)
butn_sub.configure(font=('verdana',14))

butn1= Button(root,text=1,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(1))
butn1.grid(row=3,column=0)
butn1.configure(font=('verdana',14))


butn2= Button(root,text=2,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(2))
butn2.grid(row=3,column=1)
butn2.configure(font=('verdana',14))


butn3= Button(root,text=3,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(3))
butn3.grid(row=3,column=2)
butn3.configure(font=('verdana',14))

butn_mul= Button(root,text='x',bg="green",fg="white",height=2,width=5,command=lambda: get_operators('*'))
butn_mul.grid(row=3,column=3)
butn_mul.configure(font=('verdana',14))

butn_clr= Button(root,text='C',bg="green",fg="white",height=2,width=5,command=lambda: clear())
butn_clr.grid(row=4,column=0)
butn_clr.configure(font=('verdana',14))


butn0= Button(root,text=0,bg="green",fg="white",height=2,width=5,command=lambda: get_digit(0))
butn0.grid(row=4,column=1)
butn0.configure(font=('verdana',14))


butn_equals= Button(root,text='=',bg="green",fg="white",height=2,width=5,command=lambda: get_result())
butn_equals.grid(row=4,column=2)
butn_equals.configure(font=('verdana',14))

butn_divide= Button(root,text='/',bg="green",fg="white",height=2,width=5,command=lambda: get_operators('/'))
butn_divide.grid(row=4,column=3)
butn_divide.configure(font=('verdana',14))



root.mainloop()