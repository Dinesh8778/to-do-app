from tkinter import messagebox
from tkinter import *
from json import *
import os

os.makedirs("backend", exist_ok=True)


def disable_close_event():
    if messagebox.askyesno("Quit", "Do you want to quit?"):
            root.destroy()
            dump(task,open('./backend/task.json','w'))
            dump(completed,open('./backend/completed.json','w'))

def center_window(window,width,height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

try:
    task = load(open('backend/task.json'))
    completed = load(open('backend/completed.json'))
except (JSONDecodeError,FileNotFoundError):
    task = []
    completed = []
check_vars = []

def update_labels():
    l2.config(text=f"Task remaining : {len(task)}") #config is use to update the existing lable values
    l3.config(text=f"Completed task : {len(completed)}")


def new():
    
    def add():
            if(e.get() == ""):
                messagebox.showerror("Error","Task should not be empty")
                e.focus()
            else:
                if e.get() not in task:
                    task.append(e.get())
                update_labels()
                newroot.destroy() 

    newroot = Toplevel(root)
    newroot.title("New Task")
    newroot.resizable(False,False)
    center_window(newroot,200,130)
    l = Label(newroot,text="Enter new task",font="arial 12")
    l.place(x=50,y=15)
    e = Entry(newroot,font="arial 12")
    e.focus()
    e.place(x=7,y=50)
    b = Button(newroot,text="Save",font="arial 12",command=add)
    b.place(x=77,y=80)
    newroot.protocol("WM_DELETE_WINDOW",lambda:NONE)
    
   
def view():
    check_vars.clear()
    def mark():
        remaining_task = []
        for items,var in check_vars:
            if var.get():
                if items not in completed:
                    completed.append(items)
            else:
                remaining_task.append(items)
        task[:] = remaining_task
        viewroot.destroy()
        view()

    def delete():
        remaining_task = []
        for items,var in check_vars:
            if var.get():
                task.remove(items)
            else:
                remaining_task.append(items)
        task[:] = remaining_task
        viewroot.destroy()
        view()
       
    def back():
        update_labels()
        viewroot.destroy()
        
    viewroot = Toplevel(root)
    viewroot.title("Tasks")
    viewroot.resizable(False,False)
    length = len(task)
    if(task):
        center_window(viewroot,250,(length*40)+110)
    else:
        center_window(viewroot,250,170)
    l = Label(viewroot,text="Task list",font="arial 14")
    l.place(x=80,y=15)
    index=1

    if(task):
        for index,item in enumerate(task,start=1):
            var = BooleanVar()
            l1 = Checkbutton(viewroot,text=item,font="arial 12",variable=var)
            l1.place(x=85,y=15+(index*40))
            check_vars.append((item,var))
        b1 = Button(viewroot,text="Mark as \n complete",font="arial 12",command=mark)
        b1.place(x=14,y=55+(index*40))
        b2 = Button(viewroot,text="Delete",font="arial 12",command=delete)
        b2.place(x=110,y=60+(index*40))
        b3 = Button(viewroot,text="Back",font="arial 12",command=back)
        b3.place(x=185,y=60+(index*40))
    else:
        l1 = Label(viewroot,text="---------- No tasks ----------",font="arial 12")
        l1.place(x=35,y=60)
        b3 = Button(viewroot,text="Back",font="arial 12",command=back)
        b3.place(x=95,y=60+(index*40))
    viewroot.protocol("WM_DELETE_WINDOW",lambda:NONE)

def com():

    def back():
        update_labels()
        comp.destroy()
   
    comp = Toplevel(root)
    comp.title("Completed")
    length = len(completed)
    if(completed):
        center_window(comp,250,(length*40)+110)
    else:
        center_window(comp,250,170)
    comp.resizable(False,False)
    l = Label(comp,text="Completed tasks",font="arial 14")
    l.place(x=50,y=15)
    index=1
    if(completed):
        for index,item in enumerate(completed,start=1):
            l1 = Label(comp,text=f"{index}. {item}",font="arial 12")
            l1.place(x=85,y=15+(index*40))
        b3 = Button(comp,text="Back",font="arial 12",command=back)
        b3.place(x=90,y=60+(index*40))
    else:
        l1 = Label(comp,text="---------- No tasks ----------",font="arial 12")
        l1.place(x=35,y=60)
        b3 = Button(comp,text="Back",font="arial 12",command=back)
        b3.place(x=95,y=60+(index*40))

    
    comp.protocol("WM_DELETE_WINDOW",lambda:NONE)
    

root = Tk()
root.title("To-Do app")
center_window(root,280,300)
root.resizable(False,False)

l1 = Label(root,text="Welcome to to-do app",font="arial 14")
l1.place(x=50,y=15)

b1 = Button(root,text="New Task",command=new,font="arial 12")
b1.place(x=100,y=55) 

b2 = Button(root,text="View task",command=view,font="arial 12")
b2.place(x=100,y=95) 

b3 = Button(root,text="Completed task",command=com,font="arial 12")
b3.place(x=78,y=135) 

l2 = Label(root,text=f"Task remaining : {len(task)}",font="arial 14")
l2.place(x=64,y=180) 

l3 = Label(root,text=f" Completed task : {len(completed)}",font="arial 14")
l3.place(x=64,y=215) 

b4 = Button(root,text="EXIT",font="arial 12",command=disable_close_event)
b4.place(x=115,y=255) 

root.protocol("WM_DELETE_WINDOW", disable_close_event)
root.mainloop()

