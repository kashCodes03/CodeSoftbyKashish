task = []

print("----- WELCOME TO THE TO-DO LIST MADE BY KASHISH -----")

total_task = int(input("Enter how many task do you have = "))
for i in range(1,total_task+1):
    task_name=input(f"Enter your task {i} here = ")
    task.append(task_name)
    
print(f"Today task is \n{task}")

while True:
    opration = int(input("Enter your choice what you want to do \n 1 - Add \n 2 - Update \n 3 - Del \n 4 - View \n 5 - Exit/Stop = \n"))
    if opration==1:
        add=input("Enter task you want to add = ")
        task.append(add)
        print(f"Task {add} has been added sucessfully in list")

    elif opration==2:
        updated_val = input("Enter a task name you want to update = ")
        if updated_val in task:
            up=input("Enter new task = ")
            ind=task.index(updated_val)
            task[ind]=up
    elif opration==3:
        del_val =input("Enter which task you want to del ")
        if del_val in task:
            ind=task.index(del_val)
            del task[ind]
        print("your task has been del sucessfully")
    elif opration==4:
        print(f"Total Task = {task}")
    elif opration==5:
        print("YOUR PROGRAM IS TARMINATED !! ")
        exit()
    else:
        print("invalid satement")