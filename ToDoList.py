from tkinter import *
from tkinter import messagebox

def new_task():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def delete_task():
    selected_task_index = lb.curselection()
    if selected_task_index:
        lb.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    selected_task_index = lb.curselection()
    if selected_task_index:
        updated_task = my_entry.get()
        if updated_task:
            lb.delete(selected_task_index)
            lb.insert(selected_task_index, updated_task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def clear_list():
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if confirmed:
        lb.delete(0, END)

ws = Tk()
ws.geometry('550x500')
ws.title('To-Do List')
ws.config(bg='#D2B48C')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = []


for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

add_task_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#90EE90',
    padx=20,
    pady=10,
    command=new_task
)
add_task_btn.pack(fill=BOTH, expand=True, side=LEFT)

del_task_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delete_task
)
del_task_btn.pack(fill=BOTH, expand=True, side=LEFT)

update_task_btn = Button(
    button_frame,
    text='Update Task',
    font=('times 14'),
    bg='#87CEEB',
    padx=20,
    pady=10,
    command=update_task
)
update_task_btn.pack(fill=BOTH, expand=True, side=LEFT)

clear_list_btn = Button(
    button_frame,
    text='Clear List',
    font=('times 14'),
    bg='#FFB6C1',
    padx=20,
    pady=10,
    command=clear_list
)
clear_list_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
