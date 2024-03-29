from tkinter import *

def get_digit(digit):
    current=result_label['text']
    new = current + str(digit)
    result_label.config(text=new)
    
def clear():
    result_label.config(text=" ")   

root = Tk()
root.title("Calculator")
root.geometry("424x490")
root.resizable(0,0)
root.configure(background="black")

result_label=Label(root,text=" ",bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky="w")
result_label.config(font=("verdana",40,"bold"))

btn7=Button(root,text="7", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",14))

btn8=Button(root,text="8", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("verdana",14))

btn9=Button(root,text="9", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("verdana",14))

btn_add=Button(root,text="+", bg="#ff5733",fg="white",width=8,height=3)
btn_add.grid(row=1,column=3)
btn_add.config(font=("verdana",14))


btn4=Button(root,text="4", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("verdana",14))

btn5=Button(root,text="5", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("verdana",14))

btn6=Button(root,text="6", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("verdana",14))

btn_sub=Button(root,text="-", bg="#ff5733",fg="white",width=8,height=3)
btn_sub.grid(row=2,column=3)
btn_sub.config(font=("verdana",14))


btn1=Button(root,text="1", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("verdana",14))

btn2=Button(root,text="2", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("verdana",14))

btn3=Button(root,text="3", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("verdana",14))

btn_mult=Button(root,text="*", bg="#ff5733",fg="white",width=8,height=3)
btn_mult.grid(row=3,column=3)
btn_mult.config(font=("verdana",14))

btn_clr=Button(root,text="C", bg="#ff5733",fg="white",width=8,height=3,command=lambda:clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("verdana",14))

btn0=Button(root,text="0", bg="#ff5733",fg="white",width=8,height=3,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("verdana",14))

btn_equal=Button(root,text="=", bg="#ff5733",fg="white",width=8,height=3)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=("verdana",14))

btn_div=Button(root,text="/", bg="#ff5733",fg="white",width=8,height=3)
btn_div.grid(row=4,column=3)
btn_div.config(font=("verdana",14))


root.mainloop()