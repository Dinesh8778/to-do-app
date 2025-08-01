# -- todo list app console mode 
import os

task = []
completed = []

def clear():
    os.system("cls")

def ptask():
    print("-------------")
    if(task):
        for i,j in enumerate(task, start=1):
            print(f"{i}. {j}")
        print("-------------")
    else: print("-----Nil-----")

print("Welcome to to-do app")


while(True):
    
    print("-------------")
    a = int(input("1.New task \n2.View tasks \n3.Mark complete \n4.Delete task \n5.Completed task \n6.Exit \nEnter your choice: "))
    print("-------------")
    if(a==1): # new task
        if(task.append(input("\n Enter a new task: "))):
            print("Task added sucessful")
       
    elif(a==2): # view task
        clear()
        print("Ongoing tasks")
        ptask()
    elif(a==3): # mark as complete
        clear()
        ptask()
        i = int(input("Enter S.no of task to be mark as complete "))
        completed.append(task.pop(i-1))

    elif(a==4): # delete task
        clear()
        ptask()
        i = int(input("Enter the S.no of task to be deleted "))
        task.pop(i)
    elif(a==5): # completed task
        clear()
        print("Completed tasks")
        j=0
        for i in completed:
            j = j+1
            print(j,i)
    elif(a==6): # exit
        print("--- Ended ---")
        print("-------------")
        
        break
    else: print("Wrong Input")
